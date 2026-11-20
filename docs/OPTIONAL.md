# Optional play styles — proposed profiles, not validated installs

The public **Complete** recipe is the exact enabled v0.0.3 profile. It includes 618 mod folders (including Core and local repair overlays). An alternate style must be represented by a **separate profile + dependency closure + patch/order validation + fresh-save rules**. Do not treat a checkbox in a page as proof that a patched mod can be removed safely.

| Optional edition / layer | Current baseline components to reuse | Suggested divergence | Status |
|---|---|---|---|
| **Awakened Complete** (default) | All enabled mods, Core, latest v0.0.3 patch set, local AI stack | None: full visual, quest, follower, settlement, Simonrim and roleplay experience | Exact installed recipe; static checks passed, in-game acceptance still pending |
| **Awakened Performance** | Existing eFPS, NGIO, lightweight textures and optimization patches | Adjust Community Shaders, Lux, foliage, high-poly assets, 2K texture choices and shadow/LOD quality to lower GPU/RAM cost | Candidate; must regenerate winners and review graphic dependencies |
| **Awakened Survival** | Already installed SunHelm, Campfire, Simple Hunting Overhaul, Dirt and Blood, Gourmet/Apothecary and related patches | Tune MCM difficulty, food/temperature/camping requirements, timed travel and resource scarcity | Candidate settings layer; don't concurrently enable incompatible CC Survival rule sets |
| **Awakened Story & Lore** | Alternate Start, Wyrmstooth, Bruma 1.6.4, Interesting NPCs, The Forgotten City, Clockwork, SIRENROOT, College/Companions/Thieves Guild quest fixes | De-emphasize combat/visual overhauls while keeping the narrative and AI integration | Candidate separate profile; removing a quest can break plugin masters and patches |
| **Awakened Followers** | Inigo, Lucien, Auri, Xelzaz, Remiel, Redcap, Khajiit Will Follow, their banter and quest patches | Higher companion visibility/interaction settings and roleplay rules; optionally feature specialized follower add-ons | Candidate; check NPC AI package and memory compatibility |
| **Awakened Vanilla+ / AI-First** | CHIM client/backend, Skyforge, UI, engine repairs, modest NPC improvements | Smaller world/cities/textures/followers footprint; retain persistent AI and authored dialogue | Would be a new unsupported derivative profile; not a subset safe for immediate download |
| **Awakened Visual Showcase** | Community Shaders, Skyland, Lux, Capital cities, detailed foliage, animation frameworks | Higher quality meshes, textures, LOD and optional SMP/creatures | **Not ready:** LOD generation is incomplete, high-cost options need performance and compatibility qualification |

## Disabled entries: candidates versus exclusions

The installed v0.0.3 profile also has **92 disabled entries**. [See the exhaustive table](optional-inactive-candidates.tsv), with section, source and conservative status. They are **not part of Complete** and are **not verified add-ons**.

Specific examples:

- **Alternatives, not simultaneously enabled by default:** `Immersive Music` vs the currently enabled Chapter II soundtrack; `Azurite III CS` versus the chosen Azurite Weathers III configuration; `Compass Navigation Overhaul` and Nordic skin vs the installed Infinity/Nordic UI arrangement.
- **Potential higher visual costs:** disabled `FSMP - Faster HDT-SMP`, `Fluffworks (Fluffy Animals)`, `Diverse Dragons Collection SE`, `HDR - Community Shaders` and `Upscaling - Community Shaders`.
- **Alternate quest pacing:** `At Your Own Pace` is currently disabled, not an approved plug-in to the present quest patch chain.
- **Known conflicts/exclusions:** `Barter Limit Fix` and `The Cursed Tribe - Quest Expansion` were deliberately excluded due to documented collection conflicts.
- **Testing/diagnostics:** disabled `Test - ...`, prior client versions and instrumentation must never appear as user-facing optional content.

## Optional selection rules

1. **Required** means a mod or asset is part of the exact matched Complete profile, even if the underlying feature is not everyone's taste.
2. **Feature toggle** is an existing supported MCM/INI setting with an understood compatible state, not deleting a plugin.
3. **Validated optional download** needs an independent install recipe, dependency and master audit, load-order and conflict validation, documented save requirements, and a representative runtime check.
4. **Unverified candidate** is only an idea in this document or a disabled entry in the table; it must not be offered as an easy one-click install.
5. **Known incompatible** stays excluded until its own compatibility work passes; no silent opt-in.

The user can enjoy the full baseline while the optional profiles are researched. Do not split out individual patches, plugin masters, essential animation files or AI services without proving the alternative works.
