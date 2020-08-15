# Stored Cross Site Scripting (XSS) and filter evasion

## Vulnerability
* Leave a feedback
* In the field `name`
```
<input name="txtName" type="text" size="30" maxlength="10">
```
* Remove the `maxlength` attribute
* Insert a small script like this 
```
<SCRIPT>alert('42')</SCRIPT>
```
* Submit and see popup. Note that lower case `<script>` tags are filtered.
* Write `script` or `SCRIPT` in the `name` field and submit to get the flag

## Attack
* This vulnerability allows stored XSS. Stored attacks are those where the 
injected script is permanently stored on the target servers, such as in a 
database, in a message forum, comments... The victim then retrieves the 
malicious script from the server when it requests the stored information. 
* An attacker could use a series of XSS attacks that can be used to bypass
 certain XSS defensive filters. See reference.

## Fix
* Escape all user input
* Test filtering profusely

## Reference
https://owasp.org/www-community/xss-filter-evasion-cheatsheet

