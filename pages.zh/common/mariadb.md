# mariadb

> MariaDB 客户端工具。
> 更多信息：<https://mariadb.com/kb/en/mariadb-command-line-client/>.

- 连接到特定的 MariaDB 数据库：

`mariadb {{db_name}}`

- 使用用户名和密码连接到特定的 MariaDB 数据库：

`mariadb --user {{user_name}} --password {{your_password}} {{db_name}}`

- 在交互模式和批处理模式下显示每个语句的警告：

`mariadb --show-warning`

- 减少输出的详细程度（可以多次使用以进一步减少输出）：

`mariadb {{-s|-ss|-sss|--silent}}`

- 从脚本文件中执行 SQL 语句：

`mariadb {{db_name}} < {{path/to/script.sql}} > {{path/to/output.tab}}`

- 在退出时检查内存和打开文件的使用情况：

`mariadb --debug-check`

- 使用套接字文件进行本地连接：

`mariadb {{[-S|--socket]}} {{path/to/socket_name}}`

- 显示帮助：

`mariadb {{[-?|--help]}}`