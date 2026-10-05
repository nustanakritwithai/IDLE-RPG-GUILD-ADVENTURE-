# Verified toolchain and build gates

This repository currently has no game source. Commands below describe future work on an accepted import; they have not been run by the adoption agent. The release owner's final code27 handoff must revalidate the complete toolchain and harnesses.

## Baseline identity

| Component | Verified record |
| --- | --- |
| Godot standard editor | `4.6.3.stable.official.7d41c59c4` |
| Windows console launcher SHA-256 | `63b3b2208819714c9677fbfdd8217c5b7dee8ecf5f383502e826bc9e2227ff5a` |
| Windows main editor SHA-256 | `ef90e929ba1a6a4322860285d97f40f4aa349c90329a91b0e8b55b8df0f4cb00` |
| Matching Android release template SHA-256 | `e91ef7e517e73aec1ddcc4c455c5fd53de1837c240a7c520ac438b73874b54c1` |
| Android SDK build tools | `36.1.0` |
| JDK | Eclipse Adoptium 17.0.20.1+1, x86_64; retained JDK release metadata read in place |
| Test package | `com.hearthvale.guildmaster.novice14.test` |
| ABI | ARM64 only |

The inherited code26 toolchain JSON mistakenly attached the main editor hash to the console path. The release owner's path-specific diagnostic corrected it; use the separate hashes above. No signing key contents were inspected.

Code26's tested preset is `Android Code26 Hex Test`, unsigned, versionCode 26, version `0.14.12-hex-ux-items-test`, with 271 selected resources. Its production preset remains a separate historical code25 configuration. The planned code27 test preset is `Android Code27 Guild Character Test`, versionCode 27 / 0.14.13. Its configuration is preparatory, not a completed export receipt.

## CI stages

1. **Active now:** bootstrap path allowlist, private-path/credential screening, JSON validity, preview labels and links. No engine or signing secrets are required.
2. **After source acceptance:** exact archive and per-file hashes, CRC/duplicate/traversal checks, public provenance, selected export resources, package/version/ABI, safe preset fields, and production/reset preservation.
3. **Candidate Godot check:** download only the checksum-pinned standard Linux 4.6.3 editor on an isolated GitHub-hosted runner, verify its version, import resources headlessly, and reject script/parse errors. Linux execution is not yet tested for this project. The proposed workflow is inactive until accepted.
4. **Future unsigned Android gate:** revalidate the exact JDK/SDK/template receipts against the final source handoff and vetted unsigned test preset; check script parity/import remaps, ZIP CRC and private-content exclusion, package/version/ABI, unsigned signature state, and 16 KiB ZIP/ELF alignment. Do not add signing credentials or publish an APK automatically.
5. **Release owner:** final combined gameplay/UI/character/Guild checks and separately approved signing/delivery. Desktop or headless checks do not prove physical Android behavior.

Example after an approved game import and a matching editor are available:

```text
godot --version
godot --headless --path game --import
```

Run only the handoff's approved test harnesses in fresh, isolated user profiles. Do not invent a suite list or run against real player saves. Retain each suite's actual count, failures, exit code, and error scan separately. Inherited code26 broad atomic results remain 690 checks / 112 failures, and historical 540-check continuity is deferred; no all-project-pass claim is made.

The proposed Linux archive is 71,806,687 bytes with SHA-256 `d0bc2113065e481c9c2c2b2c37daa4e8be3fe9e27f0ab9ab0b6096e9a37907f3`, as reported by the [official 4.6.3 release](https://github.com/godotengine/godot/releases/tag/4.6.3-stable). Do not download the 1.25 GB full export-template bundle during this preparation phase.

See the [Godot command-line reference](https://docs.godotengine.org/en/4.6/tutorials/editor/command_line_tutorial.html) for import and preset-specific export syntax.
