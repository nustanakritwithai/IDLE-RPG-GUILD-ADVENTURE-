# Asset provenance review

Only newly authored documentation and HTML/CSS are published in this bootstrap. No game images, sounds, fonts, generated portraits, or private provenance records are uploaded yet.

The user's public-sharing authorization is recorded. Before importing assets, preserve the asset-specific notices and resolve rights against the exact immutable handoff; public sharing does not select an open-source license for the original project.

| Family | Evidence inspected in frozen code26 | Import treatment |
| --- | --- | --- |
| Kenney Tiny Dungeon / Tiny Town | Root notices, embedded CC0 license files, vendor-lock references | Preserve CC0 text, creators/source URLs and file hashes |
| Kenney audio | Embedded pack license texts and audio notices/manifest | Preserve CC0 texts and exact provenance |
| Bobjt peacefull ville / Ansimuz Chiptune Exploration | Audio notice and admission-manifest references report CC0 | Match exact files and original-page evidence before admission |
| Noto Sans Thai / Symbols / Symbols2 | Font manifest with OFL 1.1 and license file hashes | Preserve the corresponding OFL texts and original unmodified font identities |
| Original SVG geometry/code | Project notice says original geometric work | Confirm project ownership; no blanket license invented |
| Illustrated v14.3/v14.5/v14.6, branding, 20 equipment portraits | Generated for this project with OpenAI ImageGen; hashes/prompts and current notices exist | These are explicitly not CC0. Retain provenance and applicable project/account rights; do not grant a separate art license |
| Code27 character/starter gear | Final immutable source/provenance not received | Pending release-owner handoff and review |

Raw provenance may include local paths, internal generation/Library identifiers, private Drive IDs, and creator-page snapshots. Retain those privately. Publish a sanitized derivative containing creators, public source URLs, generation method, original/runtime hashes, actual license or ownership statement, and known restrictions. Do not publish private receipt identifiers merely to preserve a historical manifest byte for byte.

The frozen originals are preserved. Before a game-source commit, require a public manifest that covers every admitted asset, identifies any reference material and rights restrictions, and retains all required notices. If a family's rights cannot be verified, hold that family and its dependent source import instead of silently substituting assets or claiming an open license.
