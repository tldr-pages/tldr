# mysqldump

> 备份 MySQL 数据库。
> 有关恢复数据库的信息，请参见 `mysql`。
> 更多信息：<https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- 创建备份（用户将被提示输入密码）：

`mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}`

- 备份特定表并将输出重定向到文件（用户将被提示输入密码）：

`mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}`

- 备份所有数据库并将输出重定向到文件（用户将被提示输入密码）：

`mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}`

- 从远程主机备份所有数据库并将输出重定向到文件（用户将被提示输入密码）：

`mysqldump --host={{ip_or_hostname}} --user {{user}} --password --all-databases > {{path/to/file.sql}}`