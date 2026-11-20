# Sauriil's Skyrim Awakened — Complete Collection

**A reference catalog, not a redistributed modpack.** This is the exact third-party side of the installed `AI-Overhaul-v0.0.3` MO2 profile, preserving names, profile order and source IDs where available. It depends on the matching [Awakened Core](CORE.md).

**Scope:** 579 third-party/reference entries, plus 39 locally produced/derived package folders in Core, for 618 enabled folders. The game itself, Steam/Skyrim DLC, official Creation Club files, MO2, Proton and external AI runtimes are separate prerequisites, not included downloads.

## Full-experience category map

| Existing MO2 section | All enabled folders | Third-party references |
|---|---:|---:|
| 80 Performance and Grass | 42 | 11 |
| 75 Sound and Music | 15 | 15 |
| 70 Lighting Weather Effects | 18 | 18 |
| 62 Cities Towns Interiors | 113 | 113 |
| 61 Followers | 20 | 20 |
| 60 New Lands | 22 | 22 |
| 52 Territory and Living World | 22 | 22 |
| 51 Quests | 32 | 28 |
| 50 NPC Behaviour and Dialogue | 44 | 44 |
| 44 Economy Equipment Travel | 23 | 22 |
| 43 Survival and Hunting | 11 | 11 |
| 42 Simonrim | 34 | 34 |
| 41 Combat and Camera | 8 | 8 |
| 40 Animation | 49 | 49 |
| 33 Characters and Faces | 14 | 14 |
| 32 Vegetation and Creatures | 26 | 26 |
| 31 Textures and Meshes | 47 | 47 |
| 30 Community Shaders | 7 | 7 |
| 20 User Interface | 8 | 8 |
| 10 AI Core | 8 | 5 |
| 01 Frameworks | 24 | 24 |
| 00 Engine and Foundation | 31 | 31 |

**What the full experience combines:**

- **Foundations and interface:** SKSE, USSEP/USMP, address library, engine repairs, SkyUI, MCM Helper, RaceMenu, Nordic UI, Infinity UI and hotkey/loot UI.
- **AI and NPC life:** CHIM's upstream dependencies, AI Overhaul SSE, Interesting NPCs, NPC dialogue expansion, authored-line integration, local inference services, follower interactions and reputation systems.
- **Quests and world:** Alternate Start – Live Another Life, the Companions/College/Thieves Guild and Icerunner improvements, quest expansions, Wyrmstooth, Beyond Skyrim Bruma **1.6.4** (not 2.x), The Forgotten City, Clockwork, SIRENROOT and Saints and Seducers Extended Cut.
- **Settlements and world changes:** JK's Skyrim/interiors, Cities of the North, Capital Whiterun/Windhelm, Great Towns/Villages, Ryn's locations, Environs, Lawbringer, Skyrim Realistic Conquering, Missives.
- **Graphics and nature:** Community Shaders and its effects, Lux/Lux Orbis/Lux Via, Azurite Weathers III, Cathedral Water, Embers XD, Skyland/SMIM, textures, grass, vegetation and creatures.
- **Motion, combat and roleplay:** Pandora and OAR, animation sets, Precision, True Directional Movement, SmoothCam, Simonrim's gameplay suite, SunHelm, Campfire, hunting and camping mods.
- **Followers:** Inigo, Lucien, Auri, Xelzaz, Remiel, Redcap and Khajiit Will Follow, with their enabled compatibility patches.

**All enabled items are part of the currently assembled full baseline.** A mod being visually optional does not mean it can safely be removed from this heavily patched load order. For alternate play styles see [OPTIONAL.md](OPTIONAL.md); each variant needs its own reviewed profile and patch closure.

## Machine-readable downloads and exact pinning

- [Every reference with original local metadata](collection-referenced-mods.tsv). Nexus URLs are taken from `meta.ini` or a recorded Nexus mod ID; file IDs and archive SHA-256 hashes come from the project's existing lockfiles only when unambiguous.
- [Every installed enabled row including Core](full-profile-all-enabled.tsv) for profile order and exact membership.
- Not every installed entry maps to a unique public archive. Some mod folders are FOMOD variants, extracted author patches or locally configured copies. A missing source URL/file ID is explicitly unresolved, **not authorization to reupload**.

## Complete alphabetic-independent reference index

The original installed group order is preserved, including patches. **Only links that exist in the local source metadata are shown**; those pages are not claims that the selected archive is currently downloadable.

### 80 Performance and Grass

- [No Grass In Objects NG](https://www.nexusmods.com/skyrimspecialedition/mods/42161) — v1.6.14, file 797980
- [Landscape Fixes For Grass Mods - Arthmoor's Town Add-ons](https://www.nexusmods.com/skyrimspecialedition/mods/9005) — v1.0.11, file 646587
- [Various Landscape Fixes For Grass Mods Patches](https://www.nexusmods.com/skyrimspecialedition/mods/128121) — v1.6.3, file 773022
- [Landscape Fixes For Grass Mods - JK's Skyrim Towns](https://www.nexusmods.com/skyrimspecialedition/mods/9005) — v1.06, file 150076
- [Landscape Fixes For Grass Mods](https://www.nexusmods.com/skyrimspecialedition/mods/9005) — v5.9, file 811138
- [Lightened Skyrim - BOS Edition](https://www.nexusmods.com/skyrimspecialedition/mods/111475) — v1.13, file 818359
- [Skyrim Project Optimization SE](https://www.nexusmods.com/skyrimspecialedition/mods/14084) — v1.5, file 263338
- [Unofficial eFPS Patches](https://www.nexusmods.com/skyrimspecialedition/mods/70176) — v1.49, file 469057
- [eFPS - Official Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/54998) — v1.7a, file 273650
- [eFPS - Anniversary Edition (Free CC)](https://www.nexusmods.com/skyrimspecialedition/mods/58727) — v1.1, file 247343
- [eFPS - Exterior FPS Boost](https://www.nexusmods.com/skyrimspecialedition/mods/54907) — v2.4.2, file 311974

### 75 Sound and Music

- [Bard Instrumentals Mostly - Sing Rarely](https://www.nexusmods.com/skyrimspecialedition/mods/10927) — v1.0, file 29425
- [Chapter II - Jeremy Soule Inspired Music](https://www.nexusmods.com/skyrimspecialedition/mods/37792) — v4, file 739020
- [Thundering Shouts](https://www.nexusmods.com/skyrimspecialedition/mods/14352) — v1.1, file 207647
- [Improved Horse Step Sounds](https://www.nexusmods.com/skyrimspecialedition/mods/848) — v3.2, file 631643
- [Solstheim Exterior Soundscapes](https://www.nexusmods.com/skyrimspecialedition/mods/121361) — v1.2, file 511919
- [Blackreach Eerie Ambience](https://www.nexusmods.com/skyrimspecialedition/mods/112114) — v2.0, file 531506
- [Distant Dragon Roars](https://www.nexusmods.com/skyrimspecialedition/mods/112185) — v1.1, file 500268
- [Acoustic Space Improvement Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/78992) — v1.3.3, file 629457
- [Reverb Interior Sounds Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/77947) — v1.5.0, file 354860
- [Regional Sounds Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/77829) — v2.1.0, file 630280
- [AOS - ISC Integration](https://www.nexusmods.com/skyrimspecialedition/mods/36761) — v1.1.0, file 280412
- [ISC SRDified](https://www.nexusmods.com/skyrimspecialedition/mods/78446) — v2.3.1, file 437740
- [Immersive Sounds - Compendium](https://www.nexusmods.com/skyrimspecialedition/mods/523) — v3.0, file 221873
- [Audio Overhaul for Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/12466) — v4.1.3, file 387525
- [UHDAP - Music HQ](https://www.nexusmods.com/skyrimspecialedition/mods/18115) — v1.0, file 57834

### 70 Lighting Weather Effects

- [Capital Windhelm and Simplicity of Snow Compatibility](https://www.nexusmods.com/skyrimspecialedition/mods/56489) — v0.5, file 232261
- [Blended Roads - Simplicity of Snow Patch](https://www.nexusmods.com/skyrimspecialedition/mods/59282) — v1.0, file 245498
- [Simplicity of Snow - Cities of The North](https://www.nexusmods.com/skyrimspecialedition/mods/58559) — v0.1, file 241931
- [Simplicity of Snow](https://www.nexusmods.com/skyrimspecialedition/mods/56235) — v0.28, file 809440
- [SRW0 Voltage](https://www.nexusmods.com/skyrimspecialedition/mods/15565) — v2, file 52703
- [Arctic - Frost Effects Redux - cubemap fix](https://www.nexusmods.com/skyrimspecialedition/mods/179296) — v1.0, file 748837
- [Arctic - Frost Effects Redux](https://www.nexusmods.com/skyrimspecialedition/mods/29817) — v3.1, file 316576
- [Embers XD](https://www.nexusmods.com/skyrimspecialedition/mods/37085) — v3.3.0, file 821729
- [Inferno - Fire Effects Redux](https://www.nexusmods.com/skyrimspecialedition/mods/29316) — v5.1, file 317399
- [Lux Orbis Misc Patches](https://www.nexusmods.com/skyrimspecialedition/mods/67610) — v1.11.0, file 666826
- [Lux Orbis - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/114169) — v4.7, file 695720
- [Lux - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/113002) — v7.2, file 810478
- [Lux Via - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/116722) — v2.2, file 490655
- [Lux Orbis](https://www.nexusmods.com/skyrimspecialedition/mods/56095) — v4.5, file 567228
- [Lux](https://www.nexusmods.com/skyrimspecialedition/mods/43158) — v7.0, file 649989
- [Lux Via](https://www.nexusmods.com/skyrimspecialedition/mods/63588) — v2.2, file 490662
- [Cathedral - Water Overhaul and Bug Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/22962) — v3.7, file 134738
- [Azurite Weathers and Seasons - Azurite Weathers III](https://www.nexusmods.com/skyrimspecialedition/mods/42731) — v3.35, file 734909

### 62 Cities Towns Interiors

- [AI Overhaul - Obscure's College of Winterhold patch](https://www.nexusmods.com/skyrimspecialedition/mods/82899) — v1.0, file 350268
- [Obscure's College of Winterhold - Script Fix - cwhcm_setchangeonquestprog_03](https://www.nexusmods.com/skyrimspecialedition/mods/62720) — v1.0, file 260213
- [Obscure's College of Winterhold](https://www.nexusmods.com/skyrimspecialedition/mods/20514) — v1.6.1, file 134566
- [Ryn's White River Watch - Skyrim Realistic Conquering AIO Patch](https://www.nexusmods.com/skyrimspecialedition/mods/132363) — v1, file 555688
- [Ryn's Lost Valley Redoubt](https://www.nexusmods.com/skyrimspecialedition/mods/102676) — v2.0, file 485594
- [Ryn's Mistwatch Folly](https://www.nexusmods.com/skyrimspecialedition/mods/79739) — v1.1, file 485580
- [Ryn's Ustengrav](https://www.nexusmods.com/skyrimspecialedition/mods/86149) — v1.0, file 364988
- [Ryn's Halted Stream Camp](https://www.nexusmods.com/skyrimspecialedition/mods/73907) — v1.5, file 383337
- [Ryn's White River Watch](https://www.nexusmods.com/skyrimspecialedition/mods/74311) — v1.6, file 383600
- [Ryn's Bleak Falls Barrow](https://www.nexusmods.com/skyrimspecialedition/mods/70984) — v1.0, file 297254
- [Ryn's Bleak Falls Tower](https://www.nexusmods.com/skyrimspecialedition/mods/72659) — v1.5, file 383262
- [Ryn's Western Watchtower](https://www.nexusmods.com/skyrimspecialedition/mods/74070) — v1.5, file 485585
- [Ryn's Skyrim patch collection (Jonado)](https://www.nexusmods.com/skyrimspecialedition/mods/128196) — v2.3.3, file 782987
- [Ryn's Dragon Mounds Collection](https://www.nexusmods.com/skyrimspecialedition/mods/85647) — v1.1.1, file 377148
- [Ryn's Standing Stones Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/76913) — v1.1, file 549102
- [Ryn's Standing Stones - Mistwatch Folly Patch](https://www.nexusmods.com/skyrimspecialedition/mods/64969) — v1, file 642795
- [Ryn's Standing Stones - Interesting NPCs Patch](https://www.nexusmods.com/skyrimspecialedition/mods/64969) — v1.2, file 271842
- [Ryn's Standing Stones](https://www.nexusmods.com/skyrimspecialedition/mods/64969) — v1.8, file 643771
- [Ryn's Farms](https://www.nexusmods.com/skyrimspecialedition/mods/72305) — v2.0, file 391452
- [Kolskeggr Mine - A Great Towns and Villages of the Reach Addon](https://www.nexusmods.com/skyrimspecialedition/mods/64265) — v1.0.0, file 266945
- [Darkwater Crossing - TGV Addon Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/64382) — v1.3, file 387217
- [Darkwater Crossing - A Great Towns and Villages of Eastmarch Addon](https://www.nexusmods.com/skyrimspecialedition/mods/64266) — v1.0.0, file 266947
- [The Great Town of Shor's Stone Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/36462) — v2.4.1, file 592872
- [The Great Town of Shor's Stone SSE](https://www.nexusmods.com/skyrimspecialedition/mods/35977) — v1.04, file 164102
- [The Great Town of Ivarstead Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/36380) — v3.5, file 725611
- [The Great Town of Ivarstead SSE](https://www.nexusmods.com/skyrimspecialedition/mods/34505) — v1.3.4, file 655006
- [The Great Town of Karthwasten Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/37471) — v3.4.1, file 816060
- [The Great Town of Karthwasten SSE](https://www.nexusmods.com/skyrimspecialedition/mods/33032) — v2.0, file 719681
- [The Great Village of Kynesgrove Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/42957) — v1.11, file 778422
- [The Great Village of Kynesgrove](https://www.nexusmods.com/skyrimspecialedition/mods/42639) — v1.1, file 213428
- [The Great Village of Old Hroldan - Fixes and Patches](https://www.nexusmods.com/skyrimspecialedition/mods/88645) — v2.1, file 606365
- [The Great Village of Old Hroldan Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/37650) — v2.4, file 409995
- [The Great Village of Old Hroldan SSE](https://www.nexusmods.com/skyrimspecialedition/mods/33189) — v1.03, file 126681
- [The Great Village of Mixwater Mill Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/37414) — v2.5, file 285159
- [The Great Village of Mixwater Mill - 3DNPC Patch (WiZkiD)](https://www.nexusmods.com/skyrimspecialedition/mods/36350) — v1.0, file 143875
- [The Great Village of Mixwater Mill SSE](https://www.nexusmods.com/skyrimspecialedition/mods/36350) — v1.1, file 213426
- [The Great Cities - Resources](https://www.nexusmods.com/skyrimspecialedition/mods/104373) — v1.1.1, file 571931
- [CWE - JK - United - JKs Candlehearth Hall - EmbersXD](https://www.nexusmods.com/skyrimspecialedition/mods/49298) — v2.3, file 201878
- [CWE - JK - United - AI Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/49298) — v1.0, file 201768
- [CWE - JK - United - JKs Candlehearth Hall](https://www.nexusmods.com/skyrimspecialedition/mods/49298) — v1.1, file 201781
- [Rob's Bug Fixes - Capital Windhelm Expansion - JK's Skyrim United](https://www.nexusmods.com/skyrimspecialedition/mods/64795) — v2.0, file 281224
- [Capital Windhelm Expansion and JK Skyrim - United](https://www.nexusmods.com/skyrimspecialedition/mods/49298) — v1.0.7, file 205418
- [Capital Windhelm Expansion Bug fixes](https://www.nexusmods.com/skyrimspecialedition/mods/93778) — v1.3.9hotfix, file 674259
- [Capital Windhelm Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/42990) — v1.3, file 188123
- [Capital Whiterun Expansion - Bucket Fix](https://www.nexusmods.com/skyrimspecialedition/mods/65422) — v1.0, file 272137
- [Capital Whiterun Expansion NPC Sleep Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/56084) — v2.00, file 256498
- [Capital Whiterun Expansion - More Accurate Collision](https://www.nexusmods.com/skyrimspecialedition/mods/66063) — v1.0, file 276340
- [GG's Capital JK's Whiterun](https://www.nexusmods.com/skyrimspecialedition/mods/93224) — v2.0, file 420635
- [Rob's Bug Fixes - Capital Whiterun Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/63355) — v3.3, file 359180
- [Capital Whiterun Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/37982) — v1.5, file 192696
- [Cities of the North - Winterhold Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/40181) — v2.17, file 629416
- [Cities of the North - Winterhold - Missives Patch](https://www.nexusmods.com/skyrimspecialedition/mods/40088) — v1.0, file 159021
- [Cities of the North - Winterhold - JK's Skyrim Patch](https://www.nexusmods.com/skyrimspecialedition/mods/40088) — v1.0, file 159459
- [Cities of the North - Winterhold](https://www.nexusmods.com/skyrimspecialedition/mods/40088) — v1.1, file 165114
- [Cities of the North - Falkreath Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/56734) — v1.29, file 708837
- [Cities of the North - Falkreath](https://www.nexusmods.com/skyrimspecialedition/mods/56731) — v1.3, file 377972
- [Cities of the North - Morthal Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/34228) — v3.7, file 724152
- [Cities of the North - Morthal](https://www.nexusmods.com/skyrimspecialedition/mods/34168) — v1.2, file 444269
- [Cities of the North - Dawnstar Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/30885) — v5.10, file 811241
- [Cities of the North - Dawnstar](https://www.nexusmods.com/skyrimspecialedition/mods/28952) — v1.4, file 444243
- [JK's Guild HQ Interiors Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/61416) — v1.29.1, file 745001
- [JK's Interiors Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/35910) — v5.30, file 812436
- [JK's Thieves Guild HQ](https://www.nexusmods.com/skyrimspecialedition/mods/133787) — v1.0.2, file 648590
- [JK's The Bards College](https://www.nexusmods.com/skyrimspecialedition/mods/71054) — v1.0.3, file 303904
- [JK's Sky Haven Temple](https://www.nexusmods.com/skyrimspecialedition/mods/63039) — v1.0.1, file 532831
- [JK's Nightingale Hall](https://www.nexusmods.com/skyrimspecialedition/mods/128116) — v1.0.0, file 548767
- [JK's Jorrvaskr](https://www.nexusmods.com/skyrimspecialedition/mods/60738) — v1.1.4, file 316462
- [JK's High Hrothgar](https://www.nexusmods.com/skyrimspecialedition/mods/62219) — v1.0.3, file 766995
- [JK's Fort Dawnguard](https://www.nexusmods.com/skyrimspecialedition/mods/110645) — v1.0.3, file 650940
- [JK's Dark Brotherhood Sanctuaries](https://www.nexusmods.com/skyrimspecialedition/mods/121950) — v1.1.1, file 761858
- [JK's Castle Volkihar](https://www.nexusmods.com/skyrimspecialedition/mods/116314) — v1.1.2, file 500285
- [JK's Castle Dour](https://www.nexusmods.com/skyrimspecialedition/mods/74309) — v1.3.1, file 622122
- [JK's Sinderion's Field Laboratory](https://www.nexusmods.com/skyrimspecialedition/mods/68154) — v1.2.0, file 803072
- [JK's Septimus Signus's Outpost](https://www.nexusmods.com/skyrimspecialedition/mods/66915) — v1.0.2, file 648587
- [JK's White Phial](https://www.nexusmods.com/skyrimspecialedition/mods/47713) — v1.1.1, file 196745
- [JK's Warmaiden's](https://www.nexusmods.com/skyrimspecialedition/mods/33685) — v1.3.0, file 386090
- [JK's Understone Keep](https://www.nexusmods.com/skyrimspecialedition/mods/55571) — v1.1.3, file 787062
- [JK's The Winking Skeever](https://www.nexusmods.com/skyrimspecialedition/mods/43991) — v1.6.0, file 648588
- [JK's The Temple of Mara](https://www.nexusmods.com/skyrimspecialedition/mods/52724) — v1.1, file 326432
- [JK's The Ragged Flagon](https://www.nexusmods.com/skyrimspecialedition/mods/50765) — v1.0.0, file 207199
- [JK's The Pawned Prawn](https://www.nexusmods.com/skyrimspecialedition/mods/50135) — v1.0.1, file 207546
- [JK's The Hag's Cure](https://www.nexusmods.com/skyrimspecialedition/mods/54587) — v1.0.0, file 224041
- [JK's The Drunken Huntsman](https://www.nexusmods.com/skyrimspecialedition/mods/33783) — v1.1.0, file 580937
- [JK's The Bee and Barb](https://www.nexusmods.com/skyrimspecialedition/mods/49516) — v1.1.1, file 286254
- [JK's The Bannered Mare](https://www.nexusmods.com/skyrimspecialedition/mods/33845) — v1.1.1, file 479869
- [JK's Temple of the Divines](https://www.nexusmods.com/skyrimspecialedition/mods/57304) — v1.2.0, file 298247
- [JK's Temple of Talos](https://www.nexusmods.com/skyrimspecialedition/mods/56971) — v1.1, file 244452
- [JK's Temple of Kynareth](https://www.nexusmods.com/skyrimspecialedition/mods/56737) — v1.0.0, file 236465
- [JK's Temple of Dibella](https://www.nexusmods.com/skyrimspecialedition/mods/56371) — v1.0.0, file 232671
- [JK's Sleeping Giant Inn](https://www.nexusmods.com/skyrimspecialedition/mods/35806) — v1.1.1, file 626615
- [JK's Silver-Blood Inn](https://www.nexusmods.com/skyrimspecialedition/mods/53554) — v1.0.2, file 578303
- [JK's Sadri's Used Wares](https://www.nexusmods.com/skyrimspecialedition/mods/47942) — v1.0.1, file 236673
- [JK's Riverwood Trader](https://www.nexusmods.com/skyrimspecialedition/mods/55959) — v1.1.1, file 286256
- [JK's Radiant Raiment](https://www.nexusmods.com/skyrimspecialedition/mods/44858) — v1.0.4, file 628261
- [JK's Palace of the Kings](https://www.nexusmods.com/skyrimspecialedition/mods/48902) — v1.2.0, file 244454
- [JK's Nightgate Inn](https://www.nexusmods.com/skyrimspecialedition/mods/161218) — v1.0.0, file 684456
- [JK's New Gnisis Cornerclub](https://www.nexusmods.com/skyrimspecialedition/mods/48293) — v1.1.0, file 246358
- [JK's Mistveil Keep](https://www.nexusmods.com/skyrimspecialedition/mods/52462) — v1.0.2, file 229295
- [JK's Haelga's Bunkhouse](https://www.nexusmods.com/skyrimspecialedition/mods/60085) — v1.1.1, file 265790
- [JK's Elgrim's Elixirs](https://www.nexusmods.com/skyrimspecialedition/mods/49934) — v1.1, file 335196
- [JK's Dragonsreach](https://www.nexusmods.com/skyrimspecialedition/mods/34000) — v1.1.3, file 579386
- [JK's Candlehearth Hall](https://www.nexusmods.com/skyrimspecialedition/mods/45617) — v1.0.0, file 185575
- [JK's Blue Palace](https://www.nexusmods.com/skyrimspecialedition/mods/45324) — v2.0.2, file 622815
- [JK's Bits and Pieces](https://www.nexusmods.com/skyrimspecialedition/mods/44642) — v1.0.0, file 181168
- [JK's Belethor's General Goods](https://www.nexusmods.com/skyrimspecialedition/mods/33636) — v1.1.0, file 129163
- [JK's Arnleif and Sons Trading Company](https://www.nexusmods.com/skyrimspecialedition/mods/54166) — v1.0.1, file 294543
- [JK's Arcadia's Cauldron](https://www.nexusmods.com/skyrimspecialedition/mods/33565) — v1.01, file 288019
- [JK's Angeline's Aromatics](https://www.nexusmods.com/skyrimspecialedition/mods/44482) — v1.0.0, file 180173
- [JK's Skyrim - USSEP Patch](https://www.nexusmods.com/skyrimspecialedition/mods/64346) — v1.1.1, file 659451
- [JKs Skyrim - AI Overhaul SSE Patch](https://www.nexusmods.com/skyrimspecialedition/mods/34194) — v1.4.1, file 707883
- [JK's Skyrim Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/154077) — v1.3, file 811242
- [Rob's Bug Fixes - JK's Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/63379) — v4.0, file 327771
- [JK's Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/6289) — v1.7, file 189705

### 61 Followers

- [Redcap EVG Animated Traversal Addon](https://www.nexusmods.com/skyrimspecialedition/mods/73441) — v1.1, file 330766
- [Riekling Aim Improved](https://www.nexusmods.com/skyrimspecialedition/mods/169036) — v1.0, file 706422
- [Redcap the Riekling](https://www.nexusmods.com/skyrimspecialedition/mods/73441) — v1.4.20, file 700625
- [Khajiit Will Follow - Patch - The Forgotten City](https://www.nexusmods.com/skyrimspecialedition/mods/2227) — v2.1, file 110014
- [Khajiit Will Follow - Patch - JK's Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/2227) — v1.0.1, file 635521
- [Khajiit Will Follow](https://www.nexusmods.com/skyrimspecialedition/mods/2227) — v4.7.5, file 747503
- [Remiel - Custom Voiced Dwemer Specialist and Companion](https://www.nexusmods.com/skyrimspecialedition/mods/51874) — v1.7.6, file 748194
- [Xelzaz JK's New Gnisis Cornerclub Patch](https://www.nexusmods.com/skyrimspecialedition/mods/62893) — v1.0.0, file 606745
- [Xelzaz Follower Wyrmstooth Patch](https://www.nexusmods.com/skyrimspecialedition/mods/62893) — v1.0.0, file 309601
- [Xelzaz Sirenroot Patch](https://www.nexusmods.com/skyrimspecialedition/mods/62893) — v1.0.2, file 589737
- [Xelzaz - Custom Fully Voiced Argonian Telvanni Follower](https://www.nexusmods.com/skyrimspecialedition/mods/62893) — v1.13.2, file 668058
- [Auri 3DNPC Banter Patch (fixed)](https://www.nexusmods.com/skyrimspecialedition/mods/154104) — v1.1, file 644008
- [Song of the Green Auri - Inigo Banter Patch ESLified](https://www.nexusmods.com/skyrimspecialedition/mods/101336) — v1, file 429015
- [Song of the Green (Auri Follower)](https://www.nexusmods.com/skyrimspecialedition/mods/11278) — v2.2, file 616495
- [Lucien - Creation Club - Rare Curios Patch](https://www.nexusmods.com/skyrimspecialedition/mods/20035) — v1.6.2, file 225891
- [Lucien - Beyond Skyrim - Bruma Patch](https://www.nexusmods.com/skyrimspecialedition/mods/20035) — v1.6.3a, file 338770
- [Lucien - Immersive Fully Voiced Male Follower](https://www.nexusmods.com/skyrimspecialedition/mods/20035) — v1.7.2, file 770173
- [Inigo Official Patch SE](https://www.nexusmods.com/skyrimspecialedition/mods/62868) — v2.0.0fe, file 549241
- [INIGO 2.4C UPDATE ESP FILE (xEdit-cleaned)](https://www.nexusmods.com/skyrimspecialedition/mods/89385) — v2.4C, file 378935
- [INIGO](https://www.nexusmods.com/skyrimspecialedition/mods/1461) — v2.4C, file 10496

### 60 New Lands

- [Skyrim Extended Cut - Saints and Seducers](https://www.nexusmods.com/skyrimspecialedition/mods/72772) — v1.1.3, file 792806
- [Additional Clockwork](https://www.nexusmods.com/skyrimspecialedition/mods/47087) — v3.0.6, file 735524
- [Clockwork (SSE)](https://www.nexusmods.com/skyrimspecialedition/mods/4155) — v1.0, file 7713
- [SIRENROOT - Deluge of Deceit](https://www.nexusmods.com/skyrimspecialedition/mods/70917) — v1.30, file 747488
- [Forgotten City - Softlock Protection](https://www.nexusmods.com/skyrimspecialedition/mods/66952) — v1.0, file 279022
- [Forgotten City Music Fixer](https://www.nexusmods.com/skyrimspecialedition/mods/54019) — v2.2, file 222082
- [The Forgotten City](https://www.nexusmods.com/skyrimspecialedition/mods/1179) — v1.8, file 32847
- [Interesting NPCs and Obscure's College - Mugnor Patch](https://www.nexusmods.com/skyrimspecialedition/mods/94805) — v1.1, file 402922
- [Interesting NPCs SE - Persistent Objects Restoration](https://www.nexusmods.com/skyrimspecialedition/mods/38409) — v1.1, file 151363
- [3dnpcs Fixes and Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/131274) — v6.5, file 814989
- [Interesting NPCs Infinite Loading Screen Freeze Fix](https://www.nexusmods.com/skyrimspecialedition/mods/131848) — v0.1.1, file 553928
- [Interesting NPCs (3DNPC) - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/89307) — v1.8.1, file 508515
- [Interesting NPCs SE - Cutting Room Floor Patch](https://www.nexusmods.com/skyrimspecialedition/mods/29194) — v1.0, file 130592
- [Interesting NPCs SE (3DNPC)](https://www.nexusmods.com/skyrimspecialedition/mods/29194) — v4.5, file 308366
- [Wyrmstooth CTD Fix](https://www.nexusmods.com/skyrimspecialedition/mods/127830) — v1.0, file 535965
- [Wyrmstooth](https://www.nexusmods.com/skyrimspecialedition/mods/45565) — v1.20.3, file 670394
- [Bruma and Forgotten City Patch](https://www.nexusmods.com/skyrimspecialedition/mods/27573) — v1.0, file 100152
- [SunHelm - BS Bruma Patch](https://www.nexusmods.com/skyrimspecialedition/mods/97827) — v1.0.A, file 415211
- [Timing Is Everything - Bruma Patch](https://www.nexusmods.com/skyrimspecialedition/mods/42226) — v1.0, file 170230
- [Bruma Misc Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/70920) — v1.00, file 296938
- [Beyond Skyrim - Bruma - Unofficial Fixes (UBF)](https://www.nexusmods.com/skyrimspecialedition/mods/103156) — v1.7.7, file 797173
- [Beyond Skyrim - Bruma SE](https://www.nexusmods.com/skyrimspecialedition/mods/10917) — v1.6.4, file 775191

### 52 Territory and Living World

- [Environs - Shrines of Talos - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/85141) — v3.02, file 502275
- [Environs - The Shrines of Talos](https://www.nexusmods.com/skyrimspecialedition/mods/85141) — v3.02, file 502274
- [Environs - The Greenwood Shack](https://www.nexusmods.com/skyrimspecialedition/mods/73732) — v3.0.1, file 529073
- [Environs - Hroggar's House - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/83457) — v2.0.6, file 530410
- [Environs - Hroggar's House](https://www.nexusmods.com/skyrimspecialedition/mods/83457) — v2.0.3, file 529772
- [Environs - Riften Warehouse - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/88024) — v1.02, file 478165
- [Environs - Riften Warehouse](https://www.nexusmods.com/skyrimspecialedition/mods/88024) — v2.01, file 473705
- [Environs - Abandoned Abodes - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/82410) — v1.0.4, file 532991
- [Environs - Abandoned Abodes](https://www.nexusmods.com/skyrimspecialedition/mods/82410) — v1.0.4, file 532990
- [Environs - Tundra Farmhouse - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/72981) — v3.0.4, file 592438
- [Environs - The Ruined Tundra Farmhouse](https://www.nexusmods.com/skyrimspecialedition/mods/72981) — v3.0.2, file 529079
- [Environs - Master Plugin](https://www.nexusmods.com/skyrimspecialedition/mods/91160) — v2.00, file 393237
- [After the Civil War - Siege Damage Repairs](https://www.nexusmods.com/skyrimspecialedition/mods/20668) — v2.7.2, file 792375
- [Civil War Aftermath SE](https://www.nexusmods.com/skyrimspecialedition/mods/3484) — v1.9, file 268302
- [Headhunter - Bounties Redone](https://www.nexusmods.com/skyrimspecialedition/mods/51847) — v1.61, file 755604
- [SRC - Exclude from Radiant System Options](https://www.nexusmods.com/skyrimspecialedition/mods/41881) — v1.1.4, file 678513
- [Lawbringer - Guardsman](https://www.nexusmods.com/skyrimspecialedition/mods/67003) — v1.0.37V3, file 620460
- [Lawbringer - Register and Claiming Fix](https://www.nexusmods.com/skyrimspecialedition/mods/64032) — v1, file 265922
- [Lawbringer](https://www.nexusmods.com/skyrimspecialedition/mods/29882) — v1.3.0.2, file 239677
- [Skyrim Realistic Conquering - All In One](https://www.nexusmods.com/skyrimspecialedition/mods/26396) — v0.76.1, file 679883
- [Fort Takeovers Framework](https://www.nexusmods.com/skyrimspecialedition/mods/25143) — v3.1, file 140406
- [Missives](https://www.nexusmods.com/skyrimspecialedition/mods/17576) — v2.03, file 98093

### 51 Quests

- [House of Horrors QE - SRC Patch](https://www.nexusmods.com/skyrimspecialedition/mods/57584) — v1.3.0, file 260170
- [Destroy the DB QE - Artificer Patch](https://www.nexusmods.com/skyrimspecialedition/mods/151173) — vv1.0.0, file 631840
- AI Overhaul v0.0.3 - Alternate Start Author Patches — v0.0.3, EXTRACTED AUTHOR PATCHES — reference original archives, do not bundle this folder, source link unresolved
- [Misc Dialogue Edits - Alternate Start Patch](https://www.nexusmods.com/skyrimspecialedition/mods/28904) — v1.9.5.3, file 557392
- [Alternate Start - Live Another Life](https://www.nexusmods.com/skyrimspecialedition/mods/272) — v4.2.6a, file 729409
- [Improved Companions - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22300) — v1.1, file 77033
- [Improved College Entry - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22184) — v2.8, file 165417
- [Choose Your Own Arch-Mage](https://www.nexusmods.com/skyrimspecialedition/mods/30887) — v1.0.01, file 117892
- [Save the Icerunner - Lights Out Alternate Routes](https://www.nexusmods.com/skyrimspecialedition/mods/34681) — v1.1.2, file 136157
- [Finding Susanna Alive](https://www.nexusmods.com/skyrimspecialedition/mods/32512) — v1.0, file 124236
- [The Taste of Death - Quest Addon](https://www.nexusmods.com/skyrimspecialedition/mods/123173) — v4b, file 614914
- [Thieves Guild Requirements SE](https://www.nexusmods.com/skyrimspecialedition/mods/33256) — v5.3.2, file 767030
- [Destroy The Dark Brotherhood - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/118229) — v1.03, file 520202
- [Infiltration QE - CRF Patch](https://www.nexusmods.com/skyrimspecialedition/mods/114054) — v1.02, file 535066
- [Infiltration - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/114054) — v1.02, file 535065
- [The Heart of Dibella - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/94863) — v1.07, file 619527
- [Innocence Lost - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/80974) — v1.12, file 628376
- [The Whispering Door - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/76606) — v1.15, file 696088
- [College of Winterhold - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/66666) — v1.16, file 616798
- [Caught Red Handed - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/65708) — v1.07, file 713588
- [The Only Cure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57683) — v1.05, file 559119
- [House of Horrors QE - TCIY Patch](https://www.nexusmods.com/skyrimspecialedition/mods/90617) — vV1.0, file 384467
- [House of Horrors - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57285) — v1.14, file 788389
- [Nilheim - Misc Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/53792) — v1.14, file 655965
- [Paarthurnax - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/51711) — v1.13, file 756573
- [Cutting Room Floor - SSE](https://www.nexusmods.com/skyrimspecialedition/mods/276) — v3.1.25, file 749038
- [Timing is Everything SE](https://www.nexusmods.com/skyrimspecialedition/mods/25464) — v2.2, file 103670
- [The Choice is Yours](https://www.nexusmods.com/skyrimspecialedition/mods/3850) — v2.7, file 397674

### 50 NPC Behaviour and Dialogue

- [Face Sculptor Expanded](https://www.nexusmods.com/skyrimspecialedition/mods/110116) — v1.02, file 541706
- [NPCs React To Frenzy](https://www.nexusmods.com/skyrimspecialedition/mods/107492) — v1.0, file 455878
- [NPCs React To Invisibility - Apothecary Patch](https://www.nexusmods.com/skyrimspecialedition/mods/91480) — v1.10, file 519935
- [NPCs React To Invisibility](https://www.nexusmods.com/skyrimspecialedition/mods/91480) — v1.11, file 535128
- [NPCs React To Necromancy (And More)](https://www.nexusmods.com/skyrimspecialedition/mods/70428) — v1.03, file 594711
- [Carriages and Stables Dialogue - CFTO Patch](https://www.nexusmods.com/skyrimspecialedition/mods/79297) — v1.0, file 338955
- [Carriages and Stables Dialogue Bundle](https://www.nexusmods.com/skyrimspecialedition/mods/79297) — v1.0, file 334238
- [Brawl Lines Expansion and Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/94070) — v1.02, file 403503
- [Falmer Servant Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/120995) — v1.01, file 578893
- [Additional Dremora Faces - Mysticism Patch](https://www.nexusmods.com/skyrimspecialedition/mods/152058) — v1.0, file 642765
- [Additional Dremora Faces](https://www.nexusmods.com/skyrimspecialedition/mods/97946) — v1.3.12, file 658910
- [Dremora Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/100562) — v1.1, file 432887
- [Vampire Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/83484) — v1.02, file 459574
- [Forsworn and Thalmor Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/80188) — v1.02, file 459575
- [Civil War Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/77566) — v1.1, file 523967
- [Bandit Lines Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/63733) — v1.09, file 459566
- [Immersive Rejections](https://www.nexusmods.com/skyrimspecialedition/mods/67930) — v1.13, file 461960
- [Sleeping Expanded - Animations and NPC reactions](https://www.nexusmods.com/skyrimspecialedition/mods/59250) — v1.22, file 339580
- [Multiple Floors Sandboxing](https://www.nexusmods.com/skyrimspecialedition/mods/4524) — v1.0, file 8856
- [Skyrim Reputation - Mysterious Letter Fix](https://www.nexusmods.com/skyrimspecialedition/mods/81701) — v1.0, file 345096
- [Skyrim Reputation - Infiltration QE Patch](https://www.nexusmods.com/skyrimspecialedition/mods/138386) — v1, file 580406
- [Skyrim Reputation Patches for Quest Expansions](https://www.nexusmods.com/skyrimspecialedition/mods/79631) — v2.1.0, file 607802
- [Skyrim Reputation Improved](https://www.nexusmods.com/skyrimspecialedition/mods/52416) — v1.3.3, file 224108
- [Skyrim Reputation - Fixed and Patched](https://www.nexusmods.com/skyrimspecialedition/mods/42538) — v1.2, file 176537
- [Skyrim Reputation](https://www.nexusmods.com/skyrimspecialedition/mods/22374) — v2.4, file 117415
- [Immersive Patrols SE AE](https://www.nexusmods.com/skyrimspecialedition/mods/718) — v3.0b, file 481213
- [Extended Encounters](https://www.nexusmods.com/skyrimspecialedition/mods/44810) — v1.7.1, file 769858
- [Realistic AI Detection 3](https://www.nexusmods.com/skyrimspecialedition/mods/2345) — v3.1, file 279347
- [Run For Your Lives](https://www.nexusmods.com/skyrimspecialedition/mods/2272) — v4.0.7, file 737640
- [To Your Face SE AE VR](https://www.nexusmods.com/skyrimspecialedition/mods/24720) — v1.0u, file 464059
- [Tavern AI Fix](https://www.nexusmods.com/skyrimspecialedition/mods/23107) — v1.2, file 267651
- [More Dialogue Options](https://www.nexusmods.com/skyrimspecialedition/mods/28905) — v1.5.1, file 496774
- [Misc Dialogue Edits](https://www.nexusmods.com/skyrimspecialedition/mods/28904) — v1.9.5.3, file 557392
- [More to Say - Sissel's Book Quest](https://www.nexusmods.com/skyrimspecialedition/mods/22622) — v9.0, file 358926
- [More to Say](https://www.nexusmods.com/skyrimspecialedition/mods/22622) — v9.0.2, file 359558
- [Guard Dialogue Overhaul SE](https://www.nexusmods.com/skyrimspecialedition/mods/22075) — v3.0, file 476224
- [Relationship Dialogue Overhaul - Update and MCM](https://www.nexusmods.com/skyrimspecialedition/mods/44601) — v1.1, file 810215
- [RDO - CRF - USSEP Patch - ESLified](https://www.nexusmods.com/skyrimspecialedition/mods/102846) — v1, file 434897
- [Relationship Dialogue Overhaul - RDO SE](https://www.nexusmods.com/skyrimspecialedition/mods/1187) — vFinal, file 1171
- [AI Overhaul - Various Patches](https://www.nexusmods.com/skyrimspecialedition/mods/78623) — v1.8, file 730777
- [AI Overhaul - BS Bruma Package Revert](https://www.nexusmods.com/skyrimspecialedition/mods/142748) — v1.0, file 598815
- [AI Overhaul - RDO Updated Patch](https://www.nexusmods.com/skyrimspecialedition/mods/35823) — v1.0, file 316874
- [AI Overhaul - CRF Patch](https://www.nexusmods.com/skyrimspecialedition/mods/35823) — v1.0.3, file 316871
- [AI Overhaul SSE](https://www.nexusmods.com/skyrimspecialedition/mods/21654) — v1.9.5, file 765713

### 44 Economy Equipment Travel

- [Realistic Conversations](https://www.nexusmods.com/skyrimspecialedition/mods/1717) — v2.1, file 10244
- [Simply Knock SKSE64 DLL](https://www.nexusmods.com/skyrimspecialedition/mods/24297) — v5.6, file 462957
- [Simply Knock SE](https://www.nexusmods.com/skyrimspecialedition/mods/14098) — v1.0.3, file 50365
- [SPID for Footprints](https://www.nexusmods.com/skyrimspecialedition/mods/54924) — v3.4, file 347974
- [Footprints](https://www.nexusmods.com/skyrimspecialedition/mods/3808) — v1.6.1, file 186188
- [Use Those Blankets](https://www.nexusmods.com/skyrimspecialedition/mods/75481) — v2.11, file 417054
- [Go To Bed - DAR-OAR patch (Sleeping Expanded version)](https://www.nexusmods.com/skyrimspecialedition/mods/43714) — v1.4, file 397219
- [Go to Bed](https://www.nexusmods.com/skyrimspecialedition/mods/4224) — v2.0.7, file 347179
- [I'm Walkin' Here NG Expanded](https://www.nexusmods.com/skyrimspecialedition/mods/122516) — v1.9.1, file 793973
- [Better Third Person Selection - BTPS](https://www.nexusmods.com/skyrimspecialedition/mods/64339) — v0.8.9, file 635566
- [Simple Dual Sheath](https://www.nexusmods.com/skyrimspecialedition/mods/50049) — v1.5.7, file 450438
- [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001) — v1.7.4, file 450465
- [Security Overhaul SKSE - Regional Locks](https://www.nexusmods.com/skyrimspecialedition/mods/62781) — v1.0.1, file 260861
- [Security Overhaul SKSE - Lock Variations](https://www.nexusmods.com/skyrimspecialedition/mods/58224) — v4.1.0, file 795138
- [AI Overhaul - CFTO - Patch](https://www.nexusmods.com/skyrimspecialedition/mods/109960) — v1.0, file 464167
- [Missives - Carriage and Ferry Travel Overhaul Patch](https://www.nexusmods.com/skyrimspecialedition/mods/44498) — v1.0, file 180205
- [CFTO - Companions Radiant Quest Fix](https://www.nexusmods.com/skyrimspecialedition/mods/52353) — v0.10, file 214360
- [Carriage and Ferry Travel Overhaul - Fixes and Winterhold](https://www.nexusmods.com/skyrimspecialedition/mods/40651) — v3.0, file 231504
- [Carriage and Ferry Travel Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/8379) — v2.0, file 23767
- [Honed Metal](https://www.nexusmods.com/skyrimspecialedition/mods/61015) — v1.26.1, file 507231
- [C.O.I.N. - Coins of Interesting Nature](https://www.nexusmods.com/skyrimspecialedition/mods/51439) — v3.5.3, file 765231
- [Trade and Barter](https://www.nexusmods.com/skyrimspecialedition/mods/23081) — v2.2, file 586734

### 43 Survival and Hunting

- [R.A.S.S. - Rain Ash And Snow Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/22780) — v3.5.1, file 361021
- [Immersive Carcass Carrying](https://www.nexusmods.com/skyrimspecialedition/mods/99867) — v1.00, file 423271
- [SHO - Beyond Skyrim Bruma Patch](https://www.nexusmods.com/skyrimspecialedition/mods/95943) — v1.13, file 535062
- [SHO - Gourmet Patch](https://www.nexusmods.com/skyrimspecialedition/mods/95943) — v1.10, file 495221
- [Simple Hunting Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/95943) — v1.16, file 699215
- [More Soaps - Fixed Duration](https://www.nexusmods.com/skyrimspecialedition/mods/97996) — v1.0.1, file 415714
- [More Soaps for Dirt and Blood](https://www.nexusmods.com/skyrimspecialedition/mods/52367) — v2.0, file 214490
- [Dirt and Blood - Dynamic Visual Effects](https://www.nexusmods.com/skyrimspecialedition/mods/38886) — v2.38, file 682273
- [Campfire - Complete Camping System](https://www.nexusmods.com/skyrimspecialedition/mods/667) — v1.12.1SEVR, file 65049
- [SunHelm Survival - Compatibility Patches](https://www.nexusmods.com/skyrimspecialedition/mods/41335) — v1.1, file 168682
- [SunHelm Survival and Needs](https://www.nexusmods.com/skyrimspecialedition/mods/39414) — v3.1.4, file 311142

### 42 Simonrim

- [Skyrim Reputation - Manbeast Patch](https://www.nexusmods.com/skyrimspecialedition/mods/82691) — v1.1.2, file 437499
- [Skyrim Reputation - Scion Patch](https://www.nexusmods.com/skyrimspecialedition/mods/82684) — v1.1, file 434632
- [Mysticism - Cutting Room Floor Patch](https://www.nexusmods.com/skyrimspecialedition/mods/112880) — v0.9, file 475954
- [Precision - Thaumaturgy Patch](https://www.nexusmods.com/skyrimspecialedition/mods/145873) — v1.0, file 610171
- [Precision - Mysticism Bound Weapons Patch](https://www.nexusmods.com/skyrimspecialedition/mods/139444) — v1.0, file 584771
- [Thaumaturgy - USSEP Patch](https://www.nexusmods.com/skyrimspecialedition/mods/103404) — v1.5.1, file 824435
- [Sorcerer - OCW Patch](https://www.nexusmods.com/skyrimspecialedition/mods/95212) — v1.0.0, file 404718
- [Misc Apothecary Patches](https://www.nexusmods.com/skyrimspecialedition/mods/79641) — v4.9, file 605351
- [Sunhelm - Gourmet Patch](https://www.nexusmods.com/skyrimspecialedition/mods/178071) — v1, file 744498
- [USMP - Apprentice - Aetherius Patch](https://www.nexusmods.com/skyrimspecialedition/mods/50813) — v2.15.2, file 790801
- [Candlehearth - Unofficial Patches](https://www.nexusmods.com/skyrimspecialedition/mods/98412) — v1.16, file 452726
- [Candlehearth - Tavern AI Fix Patch](https://www.nexusmods.com/skyrimspecialedition/mods/97542) — v1.1.0, file 415808
- [Candlehearth - An Inn Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/97542) — v1.1.1, file 419795
- [Journeyman - A Fast Travel Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/92220) — v1.2.0, file 771024
- [Gourmet - A Cooking Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/96876) — v1.2.0, file 767021
- [Apothecary - Wyrmstooth Patch](https://www.nexusmods.com/skyrimspecialedition/mods/52130) — v1.4.0, file 412401
- [Apothecary - Bruma Patch](https://www.nexusmods.com/skyrimspecialedition/mods/52130) — v1.4.0, file 412400
- [Apothecary - An Alchemy Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/52130) — v1.3.9, file 447818
- [Sorcerer - A Staff and Scroll Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/95196) — v1.1.0, file 787781
- [Artificer - Xavbio Textures Addon HalfRes](https://www.nexusmods.com/skyrimspecialedition/mods/99619) — v1.0.13, file 746504
- [Artificer - An Artifact Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/99619) — v1.0.11, file 469357
- [Thaumaturgy - An Enchanting Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/57138) — v1.5, file 787801
- [Pilgrim - A Religion Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/54099) — v1.3.1, file 777833
- [Stormcrown - A Shout Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/90659) — v1.1.17, file 493442
- [Manbeast - A Werewolf Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/44746) — v2.1.1, file 443146
- [Scion - A Vampire Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/41639) — v2.2.2, file 469383
- [Arena - An Encounter Zone Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/33487) — v1.2.0, file 399865
- [Blade and Blunt - A Combat Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/34549) — v4.0.2, file 791087
- [Hand to Hand - An Adamant Addon](https://www.nexusmods.com/skyrimspecialedition/mods/59790) — v2.0.1, file 790034
- [Adamant - A Perk Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/30191) — v6.0.4, file 792101
- [Mysticism - A Magic Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/27839) — v2.5.0, file 787777
- [Apprentice - A Class Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/169288) — v1.1.0, file 790359
- [Mundus - A Standing Stone Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/33411) — v1.15.1, file 792107
- [Aetherius - A Race Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/26686) — v2.15.1, file 772611

### 41 Combat and Camera

- [Dynamic Block Hit](https://www.nexusmods.com/skyrimspecialedition/mods/100570) — v1.7, file 488244
- [NPCs Take Cover - Smarter Anti-Cheese AI](https://www.nexusmods.com/skyrimspecialedition/mods/111890) — v1.02, file 754030
- [Comprehensive First Person Animation Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/87169) — v1.5.1, file 584071
- [Improved Camera SE](https://www.nexusmods.com/skyrimspecialedition/mods/93962) — v1.1.2, file 664197
- [SmoothCam](https://www.nexusmods.com/skyrimspecialedition/mods/41252) — v1.8.1, file 813109
- [TrueHUD - HUD Additions](https://www.nexusmods.com/skyrimspecialedition/mods/62775) — v1.1.9, file 454617
- [True Directional Movement](https://www.nexusmods.com/skyrimspecialedition/mods/51614) — v2.2.7, file 768996
- [Precision - Accurate Melee Collisions](https://www.nexusmods.com/skyrimspecialedition/mods/72347) — v2.0.4, file 351862

### 40 Animation

- [Goetia Animations - Conditional Shouts](https://www.nexusmods.com/skyrimspecialedition/mods/76388) — v1.4b, file 800725
- [Goetia Animations - Sneak Magic](https://www.nexusmods.com/skyrimspecialedition/mods/75482) — v1.2, file 794557
- [Goetia Animations - Enchanted Staves](https://www.nexusmods.com/skyrimspecialedition/mods/71110) — v1.7b, file 798354
- [Goetia Animations - Magic Spell Casting](https://www.nexusmods.com/skyrimspecialedition/mods/70204) — v1.5b, file 798351
- [Goetia Animations - Sprint (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/69409) — v1.0c, file 400899
- [Goetia Animations - Female Idle Walk And Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/68005) — v1.2c, file 400900
- [Goetia Animations - Male Idle Walk And Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/68625) — v1.3c, file 400901
- [Leviathan Animations II - Greatsword Sneak Locomotion And Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/99073) — v1.0, file 420060
- [Leviathan Animations II - Greatsword Power And Sprint Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/92266) — v1.2, file 798376
- [Leviathan Animations II - Greatsword Normal Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/88171) — v1.1, file 798375
- [Leviathan Animations II - Greatsword Low Stance](https://www.nexusmods.com/skyrimspecialedition/mods/86183) — v1.1, file 798373
- [Leviathan Animations II - Greatsword Non Combat Locomotion](https://www.nexusmods.com/skyrimspecialedition/mods/84201) — v1.1, file 798372
- [Leviathan Animations II - Sprint (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/82603) — v2.4c, file 400902
- [Leviathan Animations II - Female Idle Walk And Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/80760) — v2.3c, file 400903
- [Leviathan Animations II - Male Idle Walk And Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/81463) — v2.3c, file 400904
- [Leviathan Animations - Two-Handed Power Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/50545) — v1.5, file 798355
- [Leviathan Animations - Two-Handed Normal Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/48550) — v1.4, file 798356
- [Leviathan Animations - Two-Handed High Stance](https://www.nexusmods.com/skyrimspecialedition/mods/47092) — v1.5, file 798357
- [Vanargand Animations II - Sword Power Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/190166) — v1.1, file 797737
- [Vanargand Animations II - Sword Normal Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/188411) — v1.3, file 790258
- [Vanargand Animations II - Sword Low Stance](https://www.nexusmods.com/skyrimspecialedition/mods/187094) — v1.1b, file 795099
- [Vanargand Animations II - Sword Non Combat Locomotion](https://www.nexusmods.com/skyrimspecialedition/mods/186092) — v1.3b, file 795098
- [Vanargand Animations II - Unarmed Normal And Power Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/117328) — v1.1, file 798370
- [Vanargand Animations II - Unarmed Pugilism Stance](https://www.nexusmods.com/skyrimspecialedition/mods/109684) — v1.2, file 800719
- [Vanargand Animations II - Unarmed Non Combat Locomotion](https://www.nexusmods.com/skyrimspecialedition/mods/105376) — v1.0, file 445231
- [Vanargand Animations II - Sprint (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/101688) — v1.0, file 430435
- [Vanargand Animations II - Female Idle Walk and Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/100000) — v1.1, file 423561
- [Vanargand Animations II - Male Idle Walk and Run (CATA)](https://www.nexusmods.com/skyrimspecialedition/mods/99999) — v1.0, file 426905
- [Vanargand Animations - Sneak Crossbows](https://www.nexusmods.com/skyrimspecialedition/mods/67282) — v1.1, file 794541
- [Vanargand Animations - Crossbows](https://www.nexusmods.com/skyrimspecialedition/mods/66286) — v1.1, file 794553
- [Vanargand Animations - Dual Wield Sneak Thrusts](https://www.nexusmods.com/skyrimspecialedition/mods/64577) — v1.1, file 794539
- [Vanargand Animations - Dual Wield Sneak Strikes](https://www.nexusmods.com/skyrimspecialedition/mods/64216) — v1.1, file 794536
- [Vanargand Animations - One Handed Power Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/58997) — v1.3, file 798366
- [Vanargand Animations - One Handed Normal Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/58326) — v1.2, file 798365
- [Vanargand Animations - One Handed Mid Stance](https://www.nexusmods.com/skyrimspecialedition/mods/57544) — v1.4b, file 798840
- [Vanargand Animations - Archery](https://www.nexusmods.com/skyrimspecialedition/mods/60323) — v1.1, file 798359
- [Vanargand Animations - Sneak Archery](https://www.nexusmods.com/skyrimspecialedition/mods/56788) — v1.5, file 794535
- [Vanargand Animations - Sneak Strike Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/55420) — v1.2, file 794534
- [Vanargand Animations - Sneak Thrust Attacks](https://www.nexusmods.com/skyrimspecialedition/mods/55031) — v1.2, file 794533
- [Vanargand Animations - Sneak Idle Walk and Run](https://www.nexusmods.com/skyrimspecialedition/mods/54351) — v1.2, file 794529
- [Conditional Expressions](https://www.nexusmods.com/skyrimspecialedition/mods/45148) — v1.29, file 655975
- [Gesture Animation Remix (OAR)](https://www.nexusmods.com/skyrimspecialedition/mods/64420) — v2.4.0, file 760411
- [NPC Animation Remix (OAR)](https://www.nexusmods.com/skyrimspecialedition/mods/63471) — v2.4.2, file 813390
- [EVG Animated Traversal - Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/70635) — v1.3.5, file 716631
- [EVG Animated Traversal](https://www.nexusmods.com/skyrimspecialedition/mods/63232) — v2.1, file 506136
- [EVG Animation Variance](https://www.nexusmods.com/skyrimspecialedition/mods/38534) — v1.1, file 269316
- [EVG Conditional Idles](https://www.nexusmods.com/skyrimspecialedition/mods/34006) — v1.51, file 506946
- [Immersive Interactions - Animated Actions](https://www.nexusmods.com/skyrimspecialedition/mods/47670) — v1.78, file 536423
- [Assorted Animation Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/93271) — v1.02, file 416390

### 33 Characters and Faces

- [Northborn Scars](https://www.nexusmods.com/skyrimspecialedition/mods/720) — v1.3, file 2432
- [Hvergelmir's Aesthetics - Brows](https://www.nexusmods.com/skyrimspecialedition/mods/1062) — v4.1, file 85706
- [Closed Mouths for Orcs](https://www.nexusmods.com/skyrimspecialedition/mods/79049) — v1.1.0, file 340693
- [SUEMR SSE - Eye Meshes](https://www.nexusmods.com/skyrimspecialedition/mods/18147) — vv3.0, file 117237
- [High Poly Vanilla Hair](https://www.nexusmods.com/skyrimspecialedition/mods/41863) — v3.0f, file 183572
- [Vanilla hair remake](https://www.nexusmods.com/skyrimspecialedition/mods/63979) — v1.0.2, file 501460
- [Expressive Facial Animation - Female Edition](https://www.nexusmods.com/skyrimspecialedition/mods/19181) — v1.7, file 115524
- [Expressive Facial Animation - Male Edition](https://www.nexusmods.com/skyrimspecialedition/mods/19532) — v1.21, file 115593
- [Expressive Facegen Morphs SE](https://www.nexusmods.com/skyrimspecialedition/mods/35785) — v1.0, file 151138
- [Nordic Faces - Interesting NPCs (3DNPC) Addon - No SMP](https://www.nexusmods.com/skyrimspecialedition/mods/163030) — v1, file 739467
- [Nordic Faces - FaceGen Addons](https://www.nexusmods.com/skyrimspecialedition/mods/125600) — v1.9.1, file 634644
- [Nordic Faces - FaceGen - Non-SMP](https://www.nexusmods.com/skyrimspecialedition/mods/40658) — v5.0, file 509267
- [Nordic Faces - FaceGen - BSA (FaceTint)](https://www.nexusmods.com/skyrimspecialedition/mods/40658) — v5.0, file 509231
- [Nordic Faces - Textures and Body Meshes](https://www.nexusmods.com/skyrimspecialedition/mods/40658) — v5.0, file 509230

### 32 Vegetation and Creatures

- [Hvergelmir's Aesthetics - Beards](https://www.nexusmods.com/skyrimspecialedition/mods/1067) — v5.0.1, file 85745
- [Splendor - Dragon Variants SE](https://www.nexusmods.com/skyrimspecialedition/mods/9670) — v1.0.1, file 25622
- [BACP Revamp 1.3RC - Highland Cow Brown](https://www.nexusmods.com/skyrimspecialedition/mods/70493) — v1.3RC, file 422083
- [BACP Revamp 1.3RC - Highland Cow Core Files](https://www.nexusmods.com/skyrimspecialedition/mods/70493) — v1.3RC, file 422083
- [Bellyaches Animal and Creature Pack Revamp](https://www.nexusmods.com/skyrimspecialedition/mods/70493) — v1.2, file 353429
- [Bears of the North Patches](https://www.nexusmods.com/skyrimspecialedition/mods/48148) — v1.3.2, file 750823
- [Bears of the North](https://www.nexusmods.com/skyrimspecialedition/mods/47541) — v1.1, file 193903
- [Cathedral - 3D Tundra Shrubs](https://www.nexusmods.com/skyrimspecialedition/mods/108747) — v1.1, file 459428
- [Cathedral - 3D Stonecrop](https://www.nexusmods.com/skyrimspecialedition/mods/110726) — v1.2, file 469404
- [Cathedral - 3D Pine Shrubs](https://www.nexusmods.com/skyrimspecialedition/mods/94791) — v1.2, file 405900
- [Cathedral - 3D Thicket and Dead Shrub](https://www.nexusmods.com/skyrimspecialedition/mods/86392) — v1, file 365808
- [Cathedral - 3D Sword Ferns](https://www.nexusmods.com/skyrimspecialedition/mods/82978) — v4, file 399785
- [Cathedral - 3D Dragons Tongue - Orange](https://www.nexusmods.com/skyrimspecialedition/mods/85694) — v1.1, file 363168
- [Cathedral - 3D Deathbell](https://www.nexusmods.com/skyrimspecialedition/mods/76460) — v1.1, file 321269
- [Cathedral - 3D Nightshade](https://www.nexusmods.com/skyrimspecialedition/mods/81284) — v2.4, file 347159
- [Cathedral - 3D Clovers - Hybrid 3D](https://www.nexusmods.com/skyrimspecialedition/mods/68793) — v4, file 466864
- [Cathedral - 3D Thistle](https://www.nexusmods.com/skyrimspecialedition/mods/67619) — v2.1, file 351138
- [Cathedral - 3D Snow Berries - Green and Variegated](https://www.nexusmods.com/skyrimspecialedition/mods/69415) — v1.0, file 292317
- [Cathedral - 3D Lavender - Vanilla Size](https://www.nexusmods.com/skyrimspecialedition/mods/68310) — v1.3, file 285641
- [Cathedral - 3D Tundra Cotton](https://www.nexusmods.com/skyrimspecialedition/mods/68068) — v2.0, file 287564
- [Cathedral - 3D Mountain Flowers](https://www.nexusmods.com/skyrimspecialedition/mods/41312) — v2.0, file 284821
- [Mari's flora - Medium](https://www.nexusmods.com/skyrimspecialedition/mods/45952) — v1.2, file 197655
- [Skoglendi - A Grass Mod](https://www.nexusmods.com/skyrimspecialedition/mods/93944) — v1.2, file 403794
- [Happy Little Trees - Beyond Skyrim Bruma LOD Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/72283) — v1.0.0, file 302935
- [Happy Little Trees Add-On - DynDOLOD 3 (Performance)](https://www.nexusmods.com/skyrimspecialedition/mods/56907) — v2.1.2, file 607547
- [Happy Little Trees](https://www.nexusmods.com/skyrimspecialedition/mods/50961) — v2.03, file 320481

### 31 Textures and Meshes

- [Book Covers Skyrim - USSEP Update](https://www.nexusmods.com/skyrimspecialedition/mods/50615) — v1.3, file 785398
- [Book Covers Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/901) — v4.2, file 40352
- [ElSopa - HearthFires Oven Redone](https://www.nexusmods.com/skyrimspecialedition/mods/164386) — v1.0, file 687117
- [ElSopa - Talos Redone](https://www.nexusmods.com/skyrimspecialedition/mods/191325) — v1.0, file 803094
- [ElSopa - Sacks Redone](https://www.nexusmods.com/skyrimspecialedition/mods/186340) — v1, file 780804
- [ElSopa - Barrels Redone](https://www.nexusmods.com/skyrimspecialedition/mods/185211) — v4, file 776325
- [ElSopa - Carts Redone](https://www.nexusmods.com/skyrimspecialedition/mods/187878) — v1, file 787624
- [ElSopa - High Quality Buckets SE](https://www.nexusmods.com/skyrimspecialedition/mods/47227) — v1.1, file 192381
- [ElSopa - Tankard HD](https://www.nexusmods.com/skyrimspecialedition/mods/43764) — v1.0, file 176611
- [ElSopa HD - Unique Hand Made Signs Overhaul SE](https://www.nexusmods.com/skyrimspecialedition/mods/21704) — v1.0, file 74448
- [ElSopa HD - Meridias Beacon SE](https://www.nexusmods.com/skyrimspecialedition/mods/22046) — v1.0, file 75864
- [ElSopa - Glorious HD Amulets SE](https://www.nexusmods.com/skyrimspecialedition/mods/38194) — v1.0, file 149934
- [ElSopa - Training Dummies Redone](https://www.nexusmods.com/skyrimspecialedition/mods/102948) — v1.0, file 435352
- [ElSopa - Gem Holders Redone](https://www.nexusmods.com/skyrimspecialedition/mods/110627) — v1.0, file 466737
- [ElSopa - Safe And Strongbox Redone](https://www.nexusmods.com/skyrimspecialedition/mods/109535) — v1.0, file 462467
- [ElSopa - Azura's Star Redone SE](https://www.nexusmods.com/skyrimspecialedition/mods/72011) — v1.0, file 301657
- [ElSopa - HD Grindstone Redone SE](https://www.nexusmods.com/skyrimspecialedition/mods/58149) — v1.0, file 240023
- [ElSopa - HD Iron Tools Redone SE](https://www.nexusmods.com/skyrimspecialedition/mods/60495) — v1.0, file 250888
- [ElSopa - Skeleton Key Redone](https://www.nexusmods.com/skyrimspecialedition/mods/85504) — v1.0, file 362067
- [ElSopa - HD Keys Redone SE](https://www.nexusmods.com/skyrimspecialedition/mods/48209) — v1.0, file 196464
- [ElSopa - Quivers Redone SE](https://www.nexusmods.com/skyrimspecialedition/mods/65921) — v1.0, file 274522
- [ElSopa - Potions Redone](https://www.nexusmods.com/skyrimspecialedition/mods/80832) — v1.0, file 341442
- [ElSopa - HD Medieval Anvil SE](https://www.nexusmods.com/skyrimspecialedition/mods/48825) — v1.0, file 199297
- [Daedric Armors and Weapons Retexture SE - Half Res](https://www.nexusmods.com/skyrimspecialedition/mods/84151) — v2.0.1, file 714279
- [Guards and Stormcloaks Armors Retexture SE - Half Res](https://www.nexusmods.com/skyrimspecialedition/mods/98115) — v1.1.1, file 761956
- [Frankly HD Masque of Clavicus Vile 2k](https://www.nexusmods.com/skyrimspecialedition/mods/28565) — v1.0, file 104446
- [Frankly HD Shrouded Armor](https://www.nexusmods.com/skyrimspecialedition/mods/18785) — v1.1, file 61496
- [Frankly HD Miraak](https://www.nexusmods.com/skyrimspecialedition/mods/19699) — v1.0, file 64768
- [Frankly HD Dragonbone and Dragonscale 2k](https://www.nexusmods.com/skyrimspecialedition/mods/25110) — v1.0, file 88740
- [Frankly HD Imperial Armor and Weapons 2k](https://www.nexusmods.com/skyrimspecialedition/mods/20848) — v1.0, file 70590
- [Frankly HD Thieves Guild Armors](https://www.nexusmods.com/skyrimspecialedition/mods/19953) — v1.0, file 66049
- [Frankly HD Nightingale Armor and Weapons](https://www.nexusmods.com/skyrimspecialedition/mods/18560) — v1.1, file 59909
- [Frankly HD Dawnguard Armor and Weapons](https://www.nexusmods.com/skyrimspecialedition/mods/19663) — v1.3, file 70809
- [RUSTIC CLOTHING - Special Edition 2K-1K](https://www.nexusmods.com/skyrimspecialedition/mods/4703) — v3.0, file 154782
- [JS Dragon Claws AE - 2k Textures](https://www.nexusmods.com/skyrimspecialedition/mods/57038) — v1.32, file 522290
- [JS Shrines of the Divines SE - 2K](https://www.nexusmods.com/skyrimspecialedition/mods/33394) — v1.3, file 282601
- [RUSTIC SOULGEMS - Special Edition](https://www.nexusmods.com/skyrimspecialedition/mods/5785) — v1.0, file 84678
- [RUSTIC WINDOWS - Special Edition 2K](https://www.nexusmods.com/skyrimspecialedition/mods/1937) — v2.0, file 133495
- [Blended Roads](https://www.nexusmods.com/skyrimspecialedition/mods/8834) — v1.7, file 133231
- [Skyland Bits and Bobs - Performance Version](https://www.nexusmods.com/skyrimspecialedition/mods/95032) — v1.91, file 538816
- [Skyland AIO](https://www.nexusmods.com/skyrimspecialedition/mods/34179) — v4.32, file 443514
- [ERM - Enhanced Rocks and Mountains - DynDOLOD Add-On](https://www.nexusmods.com/skyrimspecialedition/mods/88754) — v1.0.1, file 417049
- [Enhanced Rocks and Mountains - Complex Material and PBR (meshes)](https://www.nexusmods.com/skyrimspecialedition/mods/121336) — v1.2.1, file 810908
- [Forgotten Retex Project - Half Res](https://www.nexusmods.com/skyrimspecialedition/mods/7849) — v8.3, file 354954
- [Ruins Clutter Improved SE](https://www.nexusmods.com/skyrimspecialedition/mods/5870) — v3.2b, file 254650
- [Static Mesh Improvement Mod - SMIM](https://www.nexusmods.com/skyrimspecialedition/mods/659) — v2.08, file 59069
- [aMidianBorn Book of Silence SE](https://www.nexusmods.com/skyrimspecialedition/mods/35382) — v1.9.1, file 148088

### 30 Community Shaders

- [Wetness Effects - Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/112739) — v3.1.0, file 747765
- [Terrain Variation - Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/148123) — v1.2.0, file 809754
- [Terrain Blending - Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/157076) — v1.2.0, file 763935
- [Screen Space GI - Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/130375) — v4.2.0, file 763934
- [Skylighting - Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/139352) — v1.5.2, file 809752
- [Assorted Mesh Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/32117) — v0.148, file 825109
- [Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/86492) — v1.9.1, file 810029

### 20 User Interface

- [NORDIC UI - QuickLootIE Patch](https://www.nexusmods.com/skyrimspecialedition/mods/123469) — vv4.1.0, file 804272
- [NORDIC UI - Miscellaneous Patches](https://www.nexusmods.com/skyrimspecialedition/mods/54102) — v1.8.2, file 356937
- [NORDIC UI - Interface Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/49881) — v2.4.1, file 221209
- [Infinity UI](https://www.nexusmods.com/skyrimspecialedition/mods/74483) — v2.0.3, file 556134
- [QuickLoot IE](https://www.nexusmods.com/skyrimspecialedition/mods/120075) — v4.1.3, file 806802
- [moreHUD Inventory Edition](https://www.nexusmods.com/skyrimspecialedition/mods/18619) — v2.1.3.0, file 476424
- [moreHUD SE](https://www.nexusmods.com/skyrimspecialedition/mods/12688) — v5.2.2.0, file 336379
- [SkyHUD](https://www.nexusmods.com/skyrimspecialedition/mods/463) — v0.90B, file 61422

### 10 AI Core

- [CHIM - Custom](https://github.com/Dwemer-Dynamics/CHIM-Custom) — v0.4.3
- [CHIM - AIAgent](https://www.nexusmods.com/skyrimspecialedition/mods/126330) — v3.5.1, file 821897
- [NPCs Names Distributor](https://www.nexusmods.com/skyrimspecialedition/mods/73081) — v2.6.4, file 814538
- [Prisma UI](https://www.nexusmods.com/skyrimspecialedition/mods/148718) — v1.5.1, file 808126
- [Media Keys Fix SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/92948) — v1.0.2, file 792882

### 01 Frameworks

- [Mfg Fix NG](https://www.nexusmods.com/skyrimspecialedition/mods/133568) — v1.0.10, file 806155
- [Mfg Fix](https://www.nexusmods.com/skyrimspecialedition/mods/11669) — v1.6.1, file 320400
- [Dynamic Activation Key](https://www.nexusmods.com/skyrimspecialedition/mods/96273) — v1.02, file 421305
- [Conditional Armor Type Animations - CATA](https://www.nexusmods.com/skyrimspecialedition/mods/51507) — v1.3c, file 400908
- [Pandora Behaviour Engine Plus](https://www.nexusmods.com/skyrimspecialedition/mods/133232) — v5.0.0-beta, file 813165
- [Animation Motion Revolution](https://www.nexusmods.com/skyrimspecialedition/mods/50258) — v1.5.3, file 320113
- [Paired Animation Improvements](https://www.nexusmods.com/skyrimspecialedition/mods/99621) — v1.0.2, file 466426
- [Open Animation Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/92109) — v3.2.0, file 781784
- [Maxsu Block Overhaul](https://github.com/max-su-2019/MaxuBlockOverhaul/releases/tag/v0.24) — vv0.24
- [Container Distribution Framework](https://www.nexusmods.com/skyrimspecialedition/mods/120152) — v3.1.4, file 825171
- [Improvement Names Customized AE](https://www.nexusmods.com/skyrimspecialedition/mods/59435) — v1.5.0, file 344198
- [Inventory Interface Information Injector](https://www.nexusmods.com/skyrimspecialedition/mods/85702) — v1.1.0, file 494324
- [Constructible Object Custom Keyword System](https://www.nexusmods.com/skyrimspecialedition/mods/81409) — v1.1.1, file 493920
- [Custom Skills Framework](https://www.nexusmods.com/skyrimspecialedition/mods/41780) — v3.1.0, file 496520
- [Dual Casting Fix](https://www.nexusmods.com/skyrimspecialedition/mods/92454) — v1.0.1, file 796677
- [Lexicon SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/153176) — v0.1.4.3, file 693388
- [Actor Value Generator](https://www.nexusmods.com/skyrimspecialedition/mods/84743) — v2.2.9.4, file 703882
- [Perk Entry Point Extender](https://www.nexusmods.com/skyrimspecialedition/mods/91192) — v2.2.4.6, file 702049
- [Comprehensive Attack Rate Patch - SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/89042) — v1.1.2.15, file 717058
- [Notification Log SSE NG](https://www.nexusmods.com/skyrimspecialedition/mods/76947) — v1.4, file 323309
- [SkyPatcher](https://www.nexusmods.com/skyrimspecialedition/mods/106659) — v7.1.3, file 815495
- [Sound Record Distributor](https://www.nexusmods.com/skyrimspecialedition/mods/77815) — v1.5.4, file 794646
- [DynDOLOD DLL NG and Scripts](https://www.nexusmods.com/skyrimspecialedition/mods/97720) — vAlpha-43, file 802882
- [DynDOLOD Resources SE](https://www.nexusmods.com/skyrimspecialedition/mods/52897) — vAlpha-59, file 747879

### 00 Engine and Foundation

- [Fuz Ro D-oh](https://www.nexusmods.com/skyrimspecialedition/mods/15109) — v2.5, file 464222
- [RaceMenu](https://www.nexusmods.com/skyrimspecialedition/mods/19080) — v0.4.20.0, file 743640
- [MCM Helper](https://www.nexusmods.com/skyrimspecialedition/mods/53000) — v1.6.2, file 746161
- [UIExtensions](https://www.nexusmods.com/skyrimspecialedition/mods/17561) — v1.2.0, file 55628
- [SkyUI](https://www.nexusmods.com/skyrimspecialedition/mods/12604) — v5.2SE, file 35407
- [FormList Manipulator](https://www.nexusmods.com/skyrimspecialedition/mods/74037) — v1.8.1, file 546948
- [Base Object Swapper](https://www.nexusmods.com/skyrimspecialedition/mods/60805) — v3.5.0, file 794962
- [Keyword Item Distributor](https://www.nexusmods.com/skyrimspecialedition/mods/55728) — v4.1.0, file 794743
- [Spell Perk Item Distributor](https://www.nexusmods.com/skyrimspecialedition/mods/36869) — v7.3.3, file 795621
- [ConsoleUtilSSE NG](https://www.nexusmods.com/skyrimspecialedition/mods/76649) — v1.5.1, file 456904
- [JContainers SE](https://www.nexusmods.com/skyrimspecialedition/mods/16495) — v4.3.3, file 813180
- [PapyrusUtil AE SE](https://www.nexusmods.com/skyrimspecialedition/mods/13048) — v4.6, file 462773
- [powerofthree's Papyrus Extender](https://www.nexusmods.com/skyrimspecialedition/mods/22854) — v6.5.2, file 800720
- [More Informative Console](https://www.nexusmods.com/skyrimspecialedition/mods/19250) — v1.2.3.1, file 797682
- [Crash Logger SSE AE VR](https://www.nexusmods.com/skyrimspecialedition/mods/59818) — v1.25.0, file 792670
- [Animation Queue Fix](https://www.nexusmods.com/skyrimspecialedition/mods/82395) — v1.0.2, file 798212
- [Actor Limit Fix](https://www.nexusmods.com/skyrimspecialedition/mods/32349) — v9, file 368385
- [NPC AI Process Position Fix - NG](https://www.nexusmods.com/skyrimspecialedition/mods/69326) — v1.1.3, file 794615
- [Equip Enchantment Fix](https://www.nexusmods.com/skyrimspecialedition/mods/42839) — v1.3.7, file 807291
- [Animated Static Reload Fix - NG](https://www.nexusmods.com/skyrimspecialedition/mods/69331) — v1.0.4, file 794608
- [Sprint Sneak Movement Speed Fix](https://www.nexusmods.com/skyrimspecialedition/mods/86631) — v1.1.3, file 797229
- [SSE Display Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/34705) — v0.5.25, file 797175
- [Papyrus Tweaks NG](https://www.nexusmods.com/skyrimspecialedition/mods/77779) — v4.1.1, file 678973
- [powerofthree's Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/51073) — v1.17.1, file 794717
- [Scrambled Bugs](https://www.nexusmods.com/skyrimspecialedition/mods/43532) — v21, file 368378
- [Bug Fixes SSE](https://www.nexusmods.com/skyrimspecialedition/mods/33261) — v10, file 368384
- [SSE Engine Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/17230) — v7.0.20, file 725753
- [Unofficial Skyrim Modders Patch - USMP](https://www.nexusmods.com/skyrimspecialedition/mods/49616) — v2.6.8b, file 773384
- [Unofficial Skyrim Special Edition Patch](https://www.nexusmods.com/skyrimspecialedition/mods/266) — v4.3.8a, file 733846
- [Address Library for SKSE Plugins](https://www.nexusmods.com/skyrimspecialedition/mods/32444) — v13, file 795954
- [SKSE64 Scripts](https://www.nexusmods.com/skyrimspecialedition/mods/30379) — v2.2.8, file 792256

## What is not included in this public catalog

- Locally generated voice caches, private CHIM memories/DB, downloads or copyrighted Skyrim game assets.
- Any known-disabled mod as an optional selection by default; see the separate candidate list.
- Bruma 2.x: explicitly blocked by unresolved dependency and compatibility differences.
- Tool-generated DynDOLOD output: no qualified generated output exists yet for the final profile.
- Actual Nexus Vortex Collection metadata, installation testing or publication; these are future delivery formats, not verified here.
