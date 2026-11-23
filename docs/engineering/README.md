# Collection engineering orientation

1. Confirm the checkout, its remote and the assigned Issue. Use native Issue blockers, sub-issues and milestone metadata. Load the root and nearest scoped AGENTS.md. Codex and OpenCode read AGENTS.md directly and Claude Code imports the same file.
2. Find the owning surface. [Reference data](../../collection) and [distribution](../../LICENSING.md) are local to this repository. [System architecture](https://github.com/jikovec/sauriils-skyrim-awakened-core/tree/main/docs/architecture) and [coordination and source promotion](https://github.com/jikovec/sauriils-skyrim-awakened-core/tree/main/docs/engineering) are maintained in Core. Give each cross-repo PR an exact dependency revision and integration order.
3. Use the source command below. If a task requires an installed profile, mod archives, tooling or a private compatibility result, identify the authorized workspace owner and report the missing check until you can actually run it. Continue with public evidence in the meantime.

```bash
bash scripts/check verify
```

This requires Bash and Python 3.11+ and checks reference TSVs against the tracked summary and each other. Hosted CI additionally checks relative links and publication hygiene using the Core verifier pinned in its workflow. Adapted from the existing private Python catalog verifier, this public command deliberately needs no game tree, credentials or licensed downloads.

For [reproducible installation](https://github.com/jikovec/sauriils-skyrim-awakened/issues/1), identify exact source pins, acquisition rights, cleared Core release and an isolated install recipe. For [compatibility](https://github.com/jikovec/sauriils-skyrim-awakened/issues/4), bind tests to edition, executable/SKSE/Proton/MO2, plugin and asset winners, profile and save status. Verify quest/scene/alias ownership and conflicts with the component and load-order closure. Keep visual, audio, gameplay and owner acceptance distinct. For both lines of work, request the candidate’s exact pairing manifest from the authorized owner if it is absent. Review rights independently before public distribution. No public source test qualifies a release.

Use the [compatibility and release pairing](compatibility.md) page when changing authored integrations or documenting the effect of a Core revision.
