# mysqlbinlog

> Utility for processing MySQL binary log files.
> More information: <https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- Show events from a specific binary log file:

`mysqlbinlog {{path/to/binlog}}`

- Show entries from a binary log for a specific database:

`mysqlbinlog --database {{database_name}} {{path/to/binlog}}`

- Show events from a binary log between specific dates:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- Show events from a binary log between specific positions:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{path/to/binlog}}`

- Show binary log from a MySQL server on the given host:

`mysqlbinlog --host={{hostname}} {{path/to/binlog}}`
