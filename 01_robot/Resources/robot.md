#Robot
* Go to `/robots.txt`
* Content: 
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
* Go to `/whatever` folder
* Download stored file `htpasswd`
* Find content `root:8621ffdbc5698829397d97767ac13db3`
* The 2nd value is represented by 32 hex digits so most certainly a 128 bits MD5 hash
* since two equal string hashed with MD5 always give the same hash, it can be 
retrieved thank to a rainbow table storing strings and their corresponding MD5 hash.
It is a similar to a dictionary attack.
* https://md5decrypt.net/ is a large publicly available rainbow table
* `dragon` <-> `8621ffdbc5698829397d97767ac13db3` 
* Go to `/admin`
* Enter the common username `admin` with the password `dragon`
