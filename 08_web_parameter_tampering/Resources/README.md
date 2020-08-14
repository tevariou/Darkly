# Web parameter tampering

## Vulnerability
* Click on `SIGN IN`
* Click on `I forgot my password`
* View page source
```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```
* Change e-mail address
* Submit to get the flag

## Attack
An attacker could send the recovery mail to him in an open session or during
 a man-in-the-middle attack.

## Fix
Retrieve this kind of sensitive value directly in the backend

## Reference
https://owasp.org/www-community/attacks/Web_Parameter_Tampering
