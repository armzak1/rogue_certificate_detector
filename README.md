# rogue_certificate_detector

How to run:
1. Use [this guide](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension) to load the contents
   in ./extension/ into Firefox
2. Navigate to ./validator
3. Install all python dependencies as required
4. In `central_validator.py` fix the distant validator URLs
5. Type `python central_validator.py` to start it
6. For each distant validator, start by typing `python central_validatorN.py` (if ran locally, fix the ports beforehand)
7. In Firefox, inspect the extension in console to see the results. (In case of certificate mismatch you'll receive a notification)
