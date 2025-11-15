# mysql

> MySQL 命令行工具。
> 更多信息：<https://manned.org/mysql>.

- 连接数据库：

`mysql {{数据库名}}`

- 连接到数据库，系统将提示用户输入密码：

`mysql {{[-u|--user]}} {{用户名}} {{[-p|--password]}} {{数据库名}}`

- 连接到另一台主机上的数据库：

`mysql {{[-h|--host]}} {{数据库地址}} {{数据库名}}`

- 通过Unix套接字文件连接到数据库：

`mysql {{[-S|--socket]}} {{路径/到/socket.sock}}`

- 执行脚本文件中的SQL语句：

`mysql {{[-e|--execute]}} "source {{脚本.sql}}" {{数据库名}}`

- 从`mysqldump`创建的备份文件中恢复单个数据库（系统将提示用户输入密码）：

`mysql {{[-u|--user]}} {{用户名}} {{[-p|--password]}} {{数据库名}} < {{路径/到/备份文件.sql}}`

- 从备份中恢复所有数据库（系统将提示用户输入密码）：

`mysql {{[-u|--user]}} {{用户名}} {{[-p|--password]}} < {{路径/到/备份文件.sql}}`
