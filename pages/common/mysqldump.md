# mysqldump

> Dump database(s) and table(s) from MySQL server

- Basic options

These options are nessesary in the following examples. You need to add
these options as needed

`--host=example.com`: Connect to example.com. Ignore this to connect to
local MySQL server
`--user=username`: Specify username to connect to MySQL server
`--password`: Indicate that you want to get prompted to input password
`--result=filename`: Indicating the output filename.

- Dump a specific database

`mysqldump DATABASE_NAME`

- Dump specific table(s) in a database

`mysqldump DATABASE_NAME TABLE_NAME_1 [TABLE_NAME_2]`

- Dump everything

`mysqldump --all-databases`
