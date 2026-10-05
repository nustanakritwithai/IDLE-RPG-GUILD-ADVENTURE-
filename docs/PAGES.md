# Pages preview and web feasibility

The active Pages deployment publishes only `site/`: a static project status page with repository/documentation links and a small release-status JSON file. It does not expose private evidence, game saves, APKs, or game resources.

Pages was already configured for Actions publishing with HTTPS. The workflow checks the bootstrap before uploading a Pages artifact and deploying from `main`. Top-level token permission is `contents: read`; only the deployment job has `pages: write` and `id-token: write`, the permissions used by the Pages deployment action. No signing or app secrets are required. A pull request runs checks without deployment.

## Future playable preview

Code26 uses GDScript and the Compatibility renderer, which are promising starting conditions for a browser export. This is a feasibility inference, not a tested browser build. No Web preset or matching Web template has been accepted.

A future test needs the exact 4.6.3 Web template, a dedicated sanitized Web preset, an explicit resource allowlist, and checks for WebAssembly/WebGL 2.0, fonts, audio activation, touch controls, persistence, refresh/resume, project-path loading, mobile performance, and engine feature dependencies. Start with a single-thread export; a multithreaded export introduces cross-origin-isolation hosting requirements. Validate actual published behavior before offering a playable link.

The static site can host Godot web output only after these gates and asset redistribution review pass. An Android APK cannot be run by Pages. Do not promise a browser game based on `has_pages` metadata or an Android release.

References: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [Godot 4.6 web export requirements](https://docs.godotengine.org/en/4.6/tutorials/export/exporting_for_web.html).
