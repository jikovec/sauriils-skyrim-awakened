# Core and Collection compatibility

| Configuration | Core and Collection evidence | Game and runtime boundary | Status |
| --- | --- | --- | --- |
| v0.0.3 reference baseline | Core public source preview paired with the pinned Collection reference catalog | Skyrim SE 1.6.1170, SKSE 2.2.8, MO2, versioned Proton and local CHIM | Historical local static integration and source reference metadata. Independent acquisition, clean install, gameplay acceptance and distributable package are open. |
| Foundation source revisions | Core and Collection protected PRs, exact commit IDs and source checks | Public Linux source/synthetic fixtures | Engineering infrastructure only. No new playable profile or game release identifier. |

For a future paired release, use the same release identifier in both release records. Link exact Core source and cleared artifact hashes, the Collection revision and original file pins, runtime executable and tool/dependency versions, profile and effective load-order hashes, CHIM schema/range and migration readiness. Link evidence for install, authored compatibility, runtime, audio/visual and gameplay status. Identify the previous qualified pairing and restore procedure for each profile, backend and schema. Keep owner acceptance and publication permission attached to the exact candidate. Follow [Core release evidence rules](https://github.com/jikovec/sauriils-skyrim-awakened-core/blob/main/docs/engineering/development.md) and the [Collection delivery gate](https://github.com/jikovec/sauriils-skyrim-awakened/issues/1).
