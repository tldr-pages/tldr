# psql

> PostgreSQL 命令行客户端。
> 更多信息：<https://www.postgresql.org/docs/current/app-psql.html>。

- 连接到数据库。默认情况下，它使用当前登录用户通过端口 5432 连接到本地套接字：

`psql {{database}}`

- 连接到指定主机上运行的数据库，使用指定端口和用户名，无需密码提示：

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- 连接到数据库；用户将被提示输入密码：

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- 在给定数据库上执行单个 SQL 查询或 PostgreSQL 命令（在 shell 脚本中很有用）：

`psql -c '{{query}}' {{database}}`

- 从文件中在给定数据库上执行命令：

`psql {{database}} -f {{file.sql}}`