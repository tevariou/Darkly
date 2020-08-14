# Hidden directory

## Vulnerability
* `robots.txt` shows an `./hidden` directory
* Run python `script` to crawl to search the flag

## Attack
An attacker can freely use a web crawler to look for sensitive information which
 will ignore `robots.txt`

## Fix
* Don't hide sensitive information in the web directory
* Again`robots.txt` doesn't make a directory private
