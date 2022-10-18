# mysqlbinlog

> Utility for processing MySQL binary log files.
> More information: <https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- Show the contents of the binary log file:

`mysqlbinlog {{path/to/binlog}}`

- Show binary log of a specific database:

`mysqlbinlog --database {{database_name}} {{path/to/binlog}}`

- Show binary log in a range:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- Show binary log by using position:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{path/to/binlog}}`

- Show binary log from the MySQL server on the given host:

`mysqlbinlog --host={{host_name}} {{path/to/binlog}}`
