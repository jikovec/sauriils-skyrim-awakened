# Sauriil's Skyrim Awakened — Complete Collection

A **curated Skyrim Special Edition modlist**, based on the locally assembled v0.0.3 profile, paired with a required [custom AI and integration Core](https://github.com/jikovec/sauriils-skyrim-awakened-core).

**Status: reference-only development preview.** This repository contains **no mod archives or files** and does not constitute a working Nexus Vortex Collection or a one-click install. The original on-machine game reached static integration checks, but gameplay and the v0.0.3 new-game path have not been accepted in normal play.

## Contents

- [Complete third-party list](docs/COLLECTION.md): all 579 third-party/reference entries grouped under the 22 existing categories, with original Nexus/GitHub source links.
- [Pinned reference catalog (TSV)](collection/references.tsv): original mod-folder names, order, versions and available archive IDs/hashes; 578 entries match unique archive records.
- [Complete baseline crosswalk](collection/full-profile.tsv): all 618 enabled folders including the 39 local/derivative packages.
- [Inactive candidates (TSV)](collection/inactive.tsv): 92 disabled entries; **not automatically safe optional installs**.
- [Alternative play-style ideas](docs/OPTIONAL.md): performance, survival, story, follower, AI-first and visual variants (**not built or verified**).
- [Distribution and rights](LICENSING.md) and [AI transparency](docs/AI-TRANSPARENCY.md).
- [Baseline summary](collection/inventory-summary.json): counts and exact installed v0.0.3 profile checksums.

## Requirements / boundaries

The installed baseline targets Skyrim SE 1.6.1170 / SKSE 2.2.8 with MO2, pinned Proton and a local CHIM AI stack. Its external download dependencies and integration patches are **version-specific**. The source project does not yet ship a verified portable Windows/Vortex installation route, full Core binary package, generated LOD output, or completion proof for Background Life.

**Do not disable a mod or activate a candidate simply because its theme is optional**: installed plugins, quests, animations and patches depend on one another. Alternative styles require separately tested profiles.

## License

Our original reference list and metadata are dedicated to the public domain under **CC0-1.0** in `LICENSE`, to the extent we own them. This does **not** waive or confer any rights over third-party mod files, source projects, trade marks, art, character voices or game assets.

The linked [Core](https://github.com/jikovec/sauriils-skyrim-awakened-core) uses a separate GPL/CC-BY licensing scheme for its own original software and documentation.
