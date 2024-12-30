# mycli

> 一个用于MySQL的命令行客户端，支持自动补全和语法高亮。
> 更多信息：<https://mycli.net>。

- 使用当前用户的用户名连接到本地3306端口的数据库：

`mycli {{database_name}}`

- 连接到数据库（系统会提示输入密码）：

`mycli -u {{username}} {{database_name}}`

- 连接到另一台主机上的数据库：

`mycli -h {{database_host}} -P {{port}} -u {{username}} {{database_name}}`