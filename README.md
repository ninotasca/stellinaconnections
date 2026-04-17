# Stellina Connections static capture

This directory contains a local, non-WordPress capture of https://stellinaconnections.com/ so you can rebuild and maintain it without relying on WordPress.

## What is here

- `snapshots/`
  - raw HTML snapshots pulled from the live site
  - `manifest.json` with crawled pages/assets
- `source-assets/`
  - downloaded site assets from the live WordPress site
  - images, CSS, JS, fonts, Elementor-generated CSS, logos, etc.
- `static-mirror/`
  - a local static mirror with rewritten links to local assets
  - pages included:
    - `/`
    - `/about/`
    - `/services/`
    - `/process/`
    - `/faq/`
    - `/contact/`

## Quick preview

From this directory, run:

```bash
cd /Users/ntagent/dev/stellina/stellinaconnections/static-mirror
python3 -m http.server 8000
```

Then open:

- http://localhost:8000/

## Notes

- This is a capture/mirror of the current live site, not yet a cleaned hand-built redesign.
- The blog was not mirrored because the main request was to recreate the core marketing site pages.
- Some WordPress-specific JS/CSS is still present in the mirror because it was the fastest way to preserve the current look while removing the WordPress dependency for editing.
- Next logical step: rebuild this as a clean hand-authored static site (likely plain HTML/CSS or a small framework) using the mirrored pages/assets as source material.
