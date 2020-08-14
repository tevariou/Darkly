# Robots exclusion misuse

## Vulnerability
* Go to `http://[host]/robots.txt`. The robots.txt is a standard used by
 websites to communicate with web crawlers and other web robots. It tells
 search engine crawlers which pages or files the crawler can or can't request 
 from your site.
* Content: 
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
* Go to `/whatever` folder
* Download stored file `htpasswd`
* Find content `root:8621ffdbc5698829397d97767ac13db3`
* The 2nd value is represented by 32 hex digits so most certainly a 128 bits MD5 
hash
* Since two equal string hashed with MD5 always give the same hash, it can be 
retrieved thank to a rainbow table storing strings and their corresponding MD5 
hash. It is a similar to a dictionaray attack.
* Go to https://md5hashing.net/hash/md5/8621ffdbc5698829397d97767ac13db3
* It is a large publicly available rainbow table
* `8621ffdbc5698829397d97767ac13db3` <-> `dragon`
* Go to `/admin`
* Enter the username `root` with the password `dragon` to access the flag

## Attack
Sensitive files in the web root directory could be accessed by
an attacker. And above all, don't expose them in robots.txt which only hides
those files from webcrawlers.
 
## Fix
* Don't let sensitive files in the web root directory
* Don't leave clues in robots.txt

## Reference
https://www.softscheck.com/en/practical-tips-for-owasp-top-10-2017-7-insufficient-attack-protection/#fakerobotstxt
