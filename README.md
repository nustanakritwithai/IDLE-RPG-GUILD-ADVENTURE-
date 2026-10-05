# Idle RPG Guild Adventure

Repository adoption and release status for the Godot Android game. This initial public commit contains documentation, source hygiene CI, and a small GitHub Pages status preview.

**Game source is not imported yet. Code27 is pending final integration and testing.** The immutable code26 archive has been checked in place; it is not a browser build and is not included in this bootstrap.

## Current state

| Item | State |
| --- | --- |
| Godot baseline | 4.6.3.stable.official.7d41c59c4, standard GDScript editor |
| Verified archive baseline | code26 / 0.14.12-hex-ux-items-test |
| Next release | code27 / 0.14.13, pending the release owner's frozen handoff |
| Pages | Static release status preview; no playable game build |
| Android signing | Owned by the release owner; CI has no signing keys or passwords |
| Physical Android validation | Not claimed by this repository bootstrap |

[Open the status preview](https://nustanakritwithai.github.io/IDLE-RPG-GUILD-ADVENTURE-/).

## Repository guide

- [Adoption plan and measured import estimate](docs/ADOPTION.md)
- [Verified toolchain and future build gates](docs/BUILD.md)
- [Source allowlist and export sanitation](docs/SOURCE_POLICY.md)
- [Asset provenance review](docs/ASSET_PROVENANCE.md)
- [Pages and future web compatibility](docs/PAGES.md)

`site/` is the complete static preview. `scripts/check_source.py` verifies the bootstrap inventory and content. `.github/workflows/bootstrap.yml` checks every change and deploys the preview from `main`. The Godot workflow is retained with a `.proposed` suffix until an immutable game import and its CI gates are accepted.

Run the source check with Python 3.12 or newer:

```text
python -B scripts/check_source.py --root .
```

Game assets retain their individual licenses and notices when admitted. No blanket open-source license has been selected for original code or generated art. Public availability does not relabel third-party assets or generated art as CC0.
