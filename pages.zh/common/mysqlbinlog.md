# mysqlbinlog

> 用于处理 MySQL 二进制日志文件的工具。
> 更多信息：<https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- 显示特定二进制日志文件中的事件：

`mysqlbinlog {{path/to/binlog}}`

- 显示特定数据库的二进制日志条目：

`mysqlbinlog --database {{database_name}} {{path/to/binlog}}`

- 显示特定日期之间的二进制日志事件：

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- 显示特定位置之间的二进制日志事件：

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{path/to/binlog}}`

- 显示给定主机上的 MySQL 服务器的二进制日志：

`mysqlbinlog --host={{hostname}} {{path/to/binlog}}`