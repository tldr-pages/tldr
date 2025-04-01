# mysqld

> 启动 MySQL 数据库服务器。
> 更多信息：<https://dev.mysql.com/doc/refman/en/mysqld.html>.

- 启动 MySQL 数据库服务器：

`mysqld`

- 启动服务器，将错误消息输出到控制台：

`mysqld --console`

- 启动服务器，将日志输出保存到自定义日志文件：

`mysqld --log={{path/to/file.log}}`

- 打印默认参数及其值并退出：

`mysqld --print-defaults`

- 启动服务器，从文件中读取参数和值：

`mysqld --defaults-file={{path/to/file}}`

- 启动服务器并监听自定义端口：

`mysqld --port={{port}}`

- 显示帮助：

`mysqld --verbose --help`