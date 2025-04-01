# psql

> PostgreSQL 命令行客户端。
> 更多信息：<https://www.postgresql.org/docs/current/app-psql.html>。

- 连接到数据库。默认情况下，它使用当前登录用户通过本地套接字和端口 5432 连接：

`psql {{database}}`

- 使用指定的主机、端口和用户名连接到数据库（不会提示输入密码）：

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- 连接到数据库；用户将被提示输入密码：

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- 在指定的数据库上执行单个 SQL 查询或 PostgreSQL 命令（在 shell 脚本中非常有用）：

`psql -c '{{query}}' {{database}}`

- 从文件中执行命令到指定的数据库：

`psql {{database}} -f {{file.sql}}`
