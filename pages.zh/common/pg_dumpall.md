# pg_dumpall

> 将 PostgreSQL 数据库集群提取到脚本文件或其他归档文件中。
> 更多信息：<https://www.postgresql.org/docs/current/app-pg-dumpall.html>。

- 转储所有数据库：

`pg_dumpall > {{path/to/file.sql}}`

- 使用特定用户名转储所有数据库：

`pg_dumpall {{-U|--username}} {{username}} > {{path/to/file.sql}}`

- 与上面相同，自定义主机和端口：

`pg_dumpall -h {{host}} -p {{port}} > {{output_file.sql}}`

- 仅将数据库数据转储到 SQL 脚本文件中：

`pg_dumpall {{-a|--data-only}} > {{path/to/file.sql}}`

- 仅将模式（数据定义）转储到 SQL 脚本文件中：

`pg_dumpall -s > {{output_file.sql}}`