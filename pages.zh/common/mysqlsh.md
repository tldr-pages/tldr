# mysqlsh

> 高级命令行客户端，支持 SQL、JavaScript 和 Python。
> 它提供了管理 InnoDB 集群和文档存储集合的功能。
> 更多信息：<https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html>.

- 以交互模式启动 MySQL Shell：

`mysqlsh`

- 连接到 MySQL 服务器：

`mysqlsh --user {{username}} --host {{hostname}} --port {{port}}`

- 在服务器上执行 SQL 语句并退出：

`mysqlsh --user {{username}} --execute '{{sql_statement}}'`

- 以 JavaScript 模式启动 MySQL Shell：

`mysqlsh --js`

- 以 Python �模式启动 MySQL Shell：

`mysqlsh --py`

- 将 JSON 文档导入 MySQL 集合：

`mysqlsh --import {{path/to/file.json}} --schema {{schema_name}} --collection {{collection_name}}`

- 启用详细输出：

`mysqlsh --verbose`