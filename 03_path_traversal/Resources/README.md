# Path traversal

## Vulnerability
* Use the `page` URL parameter to navigate
* Try visiting a directory outside the web publish directory such as
 `http://[host]/?page=../`
* Reach `http://[host]/?page=../../../../../../../etc/passwd` which stores host 
system user account information (including password hash on some old system)
* Get the flag

## Attack
By manipulating variables that reference files with “dot-dot-slash (../)” 
sequences and its variations or by using absolute file paths, an attacker may 
access arbitrary files and directories stored on file system including 
application source code or configuration and critical system files.

## Fix
* Prefer working without user input when using file system calls
* Ensure the user cannot supply all parts of the path – surround it with your 
path code
* Server side path validation
* Don't store sensitive configuration files inside the web root

## Reference
https://owasp.org/www-community/attacks/Path_Traversal
