# pg_dump

> 将 PostgreSQL 数据库导出到脚本文件或其他归档文件。
> 更多信息：<https://www.postgresql.org/docs/current/app-pgdump.html>。

- 将数据库导出到 SQL 脚本文件：

`pg_dump {{db_name}} > {{output_file.sql}}`

- 与上述相同，自定义用户名：

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- 与上述相同，自定义主机和端口：

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- 将数据库导出到自定义格式的归档文件：

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`

- 仅导出数据库数据到 SQL 脚本文件：

`pg_dump -a {{db_name}} > {{path/to/output_file.sql}}`

- 仅导出数据库架构（数据定义）到 SQL 脚本文件：

`pg_dump -s {{db_name}} > {{path/to/output_file.sql}}`