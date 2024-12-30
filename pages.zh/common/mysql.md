# mysql

> MySQL 命令行工具。
> 更多信息：<https://www.mysql.com/>。

- 连接到数据库：

`mysql {{database_name}}`

- 连接到数据库，用户将被提示输入密码：

`mysql -u {{user}} --password {{database_name}}`

- 连接到另一主机上的数据库：

`mysql -h {{database_host}} {{database_name}}`

- 通过 Unix 套接字连接到数据库：

`mysql --socket {{path/to/socket.sock}}`

- 在脚本文件（批处理文件）中执行 SQL 语句：

`mysql -e "source {{filename.sql}}" {{database_name}}`

- 从使用 `mysqldump` 创建的备份中恢复数据库（用户将被提示输入密码）：

`mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}`

- 从备份中恢复所有数据库（用户将被提示输入密码）：

`mysql --user {{user}} --password < {{path/to/backup.sql}}`