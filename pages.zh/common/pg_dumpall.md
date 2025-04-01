# pg_dumpall

> 将 PostgreSQL 数据库集群导出到脚本文件或其他存档文件。
> 更多信息：<https://www.postgresql.org/docs/current/app-pg-dumpall.html>。

- 导出所有数据库：

`pg_dumpall > {{path/to/file.sql}}`

- 使用特定用户名导出所有数据库：

`pg_dumpall {{[-U|--username]}} {{username}} > {{path/to/file.sql}}`

- 与上述相同，自定义主机和端口：

`pg_dumpall {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} > {{output_file.sql}}`

- 仅将数据库数据导出到 SQL 脚本文件：

`pg_dumpall {{[-a|--data-only]}} > {{path/to/file.sql}}`

- 仅将模式（数据定义）导出到 SQL 脚本文件：

`pg_dumpall {{[-s|--schema-only]}} > {{output_file.sql}}`