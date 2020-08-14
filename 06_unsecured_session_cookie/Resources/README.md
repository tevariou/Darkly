# Unsecured session cookie

## Vulnerability
* Check for a session cookie
* See `I_am_admin` cookie with content `68934a3e9455fa72420237eb05902327`
* This value is a 32 hex digits, so most likely a MD5 hash.
* `https://md5decrypt.net/` is a large publicly available rainbow table
* `68934a3e9455fa72420237eb05902327` <-> `false`
* Replace `false` by `true` and hash `true` in a terminal
```
md5 -s "true"
```
* Replace the cookie content by the output `b326b5062b2f0e69046810717534cb09`
* Reload to get the flag

## Attack
A session token simply MD5 hashed can be easily forged by an attacker.

## Fix
* The server must have a way to trust the cookie content which can be changed
 by the end user. The content must be signed using a cryptographic secure
 algorithm such as HMAC or RSA by a trusted source. The server must then
 check the signature before resuming.
* A cookie should add the HttpOnly attribute to be inaccessible to the
 javascript Document. This precaution helps mitigate cross-site scripting (XSS) 
 attacks and thus token theft. The Secure attribute helps mitigate man-in-the
 -middle. The user agent will include the cookie in an HTTP request only if the 
 request is transmitted over a secure channel (typically HTTPS).
 
 ## Reference
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
