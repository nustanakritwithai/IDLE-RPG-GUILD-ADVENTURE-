# Source and export sanitation

Git ignore rules are a convenience. The reviewed manifest and source guard decide what may enter the public repository. Explicitly adding an ignored file is not approval.

## Proposed game source allowlist

Preserve the frozen project's relative structure under `game/`:

| Paths | Conditions |
| --- | --- |
| `project.godot`, `main.tscn`, `icon.svg` | Reviewed source configuration; preserve the release reset behavior |
| `scripts/`, `scenes/`, `hex/` | Source `.gd`, `.uid`, `.tscn`, `.tres`, shaders, and required data with a per-file manifest |
| `assets/` | Only reviewed runtime PNG/SVG/font/audio/data files and required source-side `.import` descriptors; preserve applicable notices/licenses |
| `tests/` | Current source harnesses and artificial data fixtures; exclude output, actual saves, screenshots with private data, and profiles |
| Root notices and `docs/` | Preserve asset/audio/font/Godot license notices and sanitized public provenance |
| `export_presets.cfg` | Separately reviewed sanitation: blank keystore/path/password fields, unsigned test preset, selected resource list, no machine-specific paths |
| Public manifest | Exact file SHA-256 and size, baseline identity, safe provenance, reviewed preset/resource inventory |

Keep `.uid` files and source-side files such as `image.png.import`. Exclude the `.godot/` cache and obsolete `.import/` directory. Runtime bitmap/font/audio assets are source assets; exported application binaries and toolchain copies are excluded.

## Always exclude

- `.godot`, editor settings, `.git` payloads, profiles, userdata, actual player/test saves, temporary/log/cache folders, private evidence, local Library/Drive IDs and private links.
- JKS/keystore/PEM/key/P12/PFX files, passwords, tokens, service accounts, environment secrets, and Godot `export_credentials.cfg`. Reject by path before opening a potential key.
- SDK/JDK/Godot/template/tool copies, build/dependency caches, APK/AAB/EXE/DLL/SO/PCK/WASM exports, and ZIP/archive copies.
- Unused historical payloads, original-provider source archives, and another project's SUPERHEX / Thick Edge material.

## Export rules

Godot's `all_resources` setting is not sufficient sanitation. Use an explicit selected-resource allowlist for the unsigned test preset, starting from its frozen runtime manifest. Add exclusion patterns for profiles, userdata, saves, tests, private evidence, docs/provenance, archives, credentials, editor settings, and toolchain directories as a second guard.

The code26 test preset already uses selected resources and blank credential fields; its production preset is unchanged and still uses a broader historical export filter. Public preset sanitation must be documented as a derivative change, preserving the frozen original and production/reset behavior. Do not use or edit the release owner's staging tree to prepare that derivative.

After any future export, inspect the archive independently: no private paths or credentials, intended package/version/ABI, all production script bytes accounted for, import remaps resolved, CRC and duplicate-name checks passed. Reject a signed output from the unsigned gate and verify the required 16 KiB native library/ZIP alignment. Signing stays outside CI.

The active guard intentionally allows only bootstrap files. Expand `ci/source-policy.json` only in the reviewed baseline-import PR alongside the frozen manifest and provenance. Unknown paths fail closed.
