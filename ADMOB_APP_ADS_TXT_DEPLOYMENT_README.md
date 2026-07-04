# AdMob app-ads.txt verification fix — 2026-07-04

This folder is the web-root deployment package for `https://trustedfriendcorp.org/`.

The file that Google AdMob must be able to read is:

```text
https://trustedfriendcorp.org/app-ads.txt
```

Its required contents are exactly:

```text
google.com, pub-5088634112140096, DIRECT, f08c47fec0942fa0
```

Important deployment rules:

1. Upload `app-ads.txt` to the root of the same hostname shown as the app's developer/marketing website in the App Store listing.
2. Do not upload only to `/tools/calculator/A0000006/` or `/tools/calculator/A0000007/`; those copies are reference copies only.
3. After deployment, open `https://trustedfriendcorp.org/app-ads.txt` in a browser and confirm that the page shows only the Google seller line above.
4. In AdMob, click **Check for updates** for Great Calculator and Project Milepost.
5. If App Store Connect uses another developer website hostname, deploy the same `app-ads.txt` file at that hostname's root too.
