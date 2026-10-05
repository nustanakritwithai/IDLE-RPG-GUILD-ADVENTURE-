# Repository adoption

The repository was inspected on 5 October 2026 at approximately 21:08 UTC. It was public with a configured default branch `main`, but no branch ref, files, releases, or Actions runs. Pages metadata was enabled. A later authenticated Pages read confirmed workflow publishing and HTTPS; an actual site response is verified separately after deployment.

The user authorized public repository use and Pages publication on 5 October 2026. This first import is a documentation/status bootstrap. No private delivery links, game art, APKs, signing material, or mutable code27 staging are included.

## Measured code26 baseline

Archive: `idle-guild-manager-0.14.12-code26-runnable-source-r2.zip`.

SHA-256: `f605df9ec54493355e63a654840451b7e42ca58505da15ff36b8b5059ec73962`.

| Measurement | Exact amount |
| --- | ---: |
| Archive bytes | 78,398,970 |
| Uncompressed source payload | 83,378,847 |
| Files | 635 |
| Asset files / bytes | 368 / 80,682,961 |
| Scripts / bytes | 128 / 1,655,851 |
| Hex module files / bytes | 70 / 471,939 |
| Test source files / bytes | 39 / 227,387 |

The archive hash, all file sizes and SHA-256 values, ZIP CRC reads, duplicate names, and prohibited path/extension screening passed against the external frozen manifest. Nothing was extracted. No AGENTS.md, SKILL.md, .agents, or .codex guidance was present in the archive; workspace and ancestor guidance were also checked.

This is an upper bound for the raw code26 import, not approval to copy everything. Public provenance manifests must remove local machine paths and private Library/Drive identifiers. Saved creator-page HTML evidence should stay in the private admission record. The public manifest must retain file hashes, creators, licenses, and source URLs. Sanitizing metadata produces a new manifest while the original frozen archive remains unchanged.

## First game baseline

1. Prefer the release owner's final immutable code27 ZIP, per-file manifest, exact tested toolchain, sanitized preset, provenance, and regression report. Until then, code27 remains pending.
2. If code26 is chosen instead, label it exactly as code26 and retain its limitations. Never merge a mutable partial code27 tree into that baseline.
3. Admit source under `game/`, preserving `project.godot`, scenes, scripts, assets, Hex modules, UIDs, import descriptors, tests, and license notices in their original relative locations.
4. Review the source/resource allowlist, public provenance, safe preset settings, and new manifest before making a single baseline commit. Re-read the remote head before updating it.
5. Start later changes on a named branch and open a draft PR with the baseline SHA, changed scope, validation evidence, and remaining limits. Merge only after relevant gates pass. Do not enable auto-merge or alter protection/permission settings as part of adoption.

## Allocation

This bootstrap fits the authorized 5 MiB preparation cap and retains a 300 MiB free-space reserve. No source tree, asset archive, Godot installation, build, or export is created here.

Before a game import, request a measured allocation from the coordinating parent. A conservative code26 staging plan is **180 MiB**: one approximately 80 MiB clean source tree, a bounded Git/object or packaging allowance, and small receipts. Reuse the existing ZIP and toolchain; do not create another full archive. A streamed per-file remote import is another option but must use the exact manifest, bounded buffers, and a reviewed final tree. The code27 size remains unknown until its final handoff.

No releases or tags are created by this bootstrap. The sole release owner retains Android integration, build, signing, and delivery ownership. SUPERHEX / Thick Edge belongs to a separate project and is outside this repository baseline.
