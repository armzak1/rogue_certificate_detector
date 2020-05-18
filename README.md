# rogue_certificate_detector

How to run:
1. Use [this guide](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension) to load the contents
   in ./extension/ into Firefox.
2. Navigate to ./validator
3. Type `python cert_checker_server.py` (Install dependencies as required)
4. In Firefox, inspect the extension in console to see the results. (In case of certificate mismatch you'll receive a notification)
