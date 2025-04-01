# mycli

> 一个支持自动补全和语法高亮的 MySQL、MariaDB 和 Percona 命令行客户端。
> 更多信息：<https://manned.org/mycli>。

- 连接到本地 3306 端口的数据库，使用当前用户的用户名：

`mycli {{database_name}}`

- 连接到数据库（用户将被提示输入密码）：

`mycli {{[-u|--user]}} {{username}} {{database_name}}`

- 连接到另一主机上的数据库：

`mycli {{[-h|--host]}} {{database_host}} {{[-P|--port]}} {{port}} {{[-u|--user]}} {{username}} {{database_name}}`