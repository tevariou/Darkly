# Unvalidated redirect

## Vulnerability 
* Spot redirect links like this `/index.php?page=redirect&site=[link]`
* Replace `[link]` with anything to get the flag

## Attack
An attacker could send a link to a target like this `http://host/index.php?page=redirect&site=[http://attacker.website]`
redirecting the user to a phishing website. Because the server name in the modified link is identical to the original 
site, phishing attempts may have a more trustworthy appearance. Unvalidated redirect can also be used to maliciously 
craft a URL that would pass the application's access control check and then forward the attacker to privileged functions 
that they would normally not be able to access.

## Fix
* Avoid using redirects
* Don't allow user input
* Implement parameters validation to authorize only valid redirects
* Allow only static links
* Warn user before redirect

## Reference
https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md
