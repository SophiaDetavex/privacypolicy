# Great Calculator public site

This directory contains the current public website for **Great Calculator**, a local-first all-in-one calculator app for iPhone and iPad.

It is designed to support the app’s public-facing marketing, privacy, privacy choices, support, accessibility, age-suitability, license, and content-rights links.

## Current revision

- Revision marker: `2026-06-24-a0000006-release-1-3-3-build-268`
- Effective date: June 24, 2026
- Canonical hosted base URL: `https://trustedfriendcorp.org/tools/calculator/A0000006/`
- Landing page / Marketing URL: `https://trustedfriendcorp.org/tools/calculator/A0000006/`
- App Store URL: `https://apps.apple.com/us/app/great-calculator/id6761633974`

## Included pages

- `index.html` — product landing page / marketing URL
- `features/index.html` — detailed feature guide
- `privacy/index.html` — privacy policy
- `privacy-choices/index.html` — privacy choices page
- `support/index.html` — support and feature-request page
- `accessibility/index.html` — accessibility posture and test checklist
- `age-suitability/index.html` — age-rating context page
- `license-agreement/index.html` — license reference page
- `eula/index.html` — full public license terms
- `content-rights/index.html` — content and external data-source rights page
- `404.html` — not-found page

Redirect wrappers such as `privacy-policy.html`, `support.html`, and `features.html` are retained so older App Store metadata, browser bookmarks, and in-app links do not break.

## Commercial-grade positioning updates

This revision preserves the iPhone/iPad launch positioning, keeps the public App Store product-page link, synchronizes the app-bundled and packaged website copies, and discloses the free app’s consent-gated Google AdMob integration: one small 320-by-50-point banner in a dedicated top lane that remains separate from the hamburger menu and calculator controls.

## App Store-facing URLs

Use these URLs in App Store Connect and in-app metadata:

- Marketing: `https://trustedfriendcorp.org/tools/calculator/A0000006/`
- Privacy Policy: `https://trustedfriendcorp.org/tools/calculator/A0000006/privacy/`
- Support: `https://trustedfriendcorp.org/tools/calculator/A0000006/support/`
- Accessibility: `https://trustedfriendcorp.org/tools/calculator/A0000006/accessibility/`
- Privacy Choices: `https://trustedfriendcorp.org/tools/calculator/A0000006/privacy-choices/`
- App Store: `https://apps.apple.com/us/app/great-calculator/id6761633974`

## Maintenance notes

Keep this public website synchronized with the shipping app. Update the site if calculator modes, platform support, orientation support, network behavior, privacy behavior, accessibility claims, support contacts, or legal terms change.

## Local validation

Run these network-free checks before deployment:

```bash
python3 scripts/validate_public_web_static_quality.py --strict
python3 scripts/validate_public_web_local_parity.py --require-packaged-site
```

Use `scripts/validate_public_web_parity.py --strict` only after the hosted GitHub Pages copy has been redeployed and should exactly match the repository copy.
