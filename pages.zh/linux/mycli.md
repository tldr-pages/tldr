# mycli

> 一个用于 MySQL、MariaDB 和 Percona 的命令行工具，支持自动补全和语法高亮。
> 更多信息：<https://manned.org/mycli>。

- 使用当前登录用户连接到数据库：

`mycli {{database_name}}`

- 使用指定用户连接到数据库：

`mycli -u {{user}} {{database_name}}`

- 使用指定用户在指定主机上连接到数据库：

`mycli -u {{user}} -h {{host}} {{database_name}}`