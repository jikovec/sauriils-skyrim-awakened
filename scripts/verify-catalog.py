"""Verify the published source catalog without an installed game or download access."""

from collections import Counter
import csv
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

CATALOG = Path(__file__).resolve().parents[1] / "collection"
IDENTITY = ("priority_line", "section", "name", "modid", "version", "repository", "url")
ENABLED = IDENTITY + ("installationFile", "nexus_file_id", "archive_sha256",
                      "archive_lock", "lock_match", "ownership_class", "publication")


def require(valid, message):
    if not valid:
        raise ValueError(message)


def read_table(name, fields):
    rows = {}
    with (CATALOG / name).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t", strict=True)
        require(tuple(reader.fieldnames or ()) == fields, f"{name}: unexpected columns")
        for row in reader:
            require(None not in row and all(value is not None for value in row.values()),
                    f"{name}:{reader.line_num}: ragged row")
            priority = row["priority_line"]
            require(re.fullmatch(r"[1-9][0-9]*", priority) and priority not in rows,
                    f"{name}:{reader.line_num}: invalid or duplicate priority")
            require(row["name"] and row["section"], f"{name}:{reader.line_num}: missing name or section")
            rows[priority] = row
    require(len({row["name"] for row in rows.values()}) == len(rows), f"{name}: duplicate names")
    return rows


def sha256(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def verify():
    full = read_table("full-profile.tsv", ENABLED)
    references = read_table("references.tsv", ENABLED)
    inactive = read_table("inactive.tsv", IDENTITY + ("option_status",))
    summary = json.loads((CATALOG / "inventory-summary.json").read_text(encoding="utf-8"))
    require(full and references, "empty enabled catalog")
    require(not (full.keys() & inactive.keys()), "enabled and inactive priorities overlap")
    require(not ({row["name"] for row in full.values()} & {row["name"] for row in inactive.values()}),
            "enabled and inactive names overlap")

    expected_refs = {key for key, row in full.items()
                     if row["ownership_class"] in {"external-reference", "third-party-extracted-repack"}}
    require(references.keys() == expected_refs, "external crosswalk coverage differs")
    require(all(full[key] == row for key, row in references.items()), "reference crosswalk rows differ")
    counts = {
        "enabled_mod_folders": len(full),
        "external_reference_folders": len(references),
        "core_or_derived_folders": len(full) - len(references),
        "disabled_candidates": len(inactive),
        "sections": dict(Counter(row["section"] for row in full.values())),
        "local_classes": dict(Counter(row["ownership_class"] for key, row in full.items()
                                      if key not in references)),
        "locked_archives": sum(row["lock_match"] == "exact" for row in full.values()),
        "nexus_source_entries": sum(row["repository"] == "Nexus" for row in full.values()),
    }
    for field, expected in counts.items():
        require(summary[field] == expected, f"summary mismatch: {field} should be {expected}")
    require(all(sha256(summary[f"{file}_sha256"]) for file in ("modlist", "plugins", "loadorder")),
            "invalid recorded profile digest")

    for key, row in full.items():
        locked = row["lock_match"] == "exact"
        require(row["lock_match"] in {"exact", "unmapped"}, f"priority {key}: unknown lock state")
        require(locked == sha256(row["archive_sha256"])
                and (locked or not row["archive_sha256"]),
                f"priority {key}: digest does not match lock state")
        role = row["ownership_class"]
        require(row["publication"] == (
            "reference-only" if role == "external-reference" else "licence-and-provenance-review-required"
        ), f"priority {key}: inconsistent rights disposition")
        if role == "external-reference":
            origin = urlsplit(row["url"])
            require(origin.scheme == "https" and origin.hostname and not origin.username,
                    f"priority {key}: invalid reference origin")
        if role == "third-party-extracted-repack":
            require(not locked, f"priority {key}: repack requires an original source and rights review")
    print(f"PASS: {len(full)} enabled, {len(references)} references, {len(inactive)} inactive")


if __name__ == "__main__":
    verify()
