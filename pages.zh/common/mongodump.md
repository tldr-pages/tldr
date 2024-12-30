# mongodump

> 用于导出 MongoDB 实例内容的工具。
> 更多信息：<https://docs.mongodb.com/database-tools/mongodump/>.

- 创建所有数据库的转储（这将把文件放在名为“dump”的目录中）：

`mongodump`

- 指定转储的输出位置：

`mongodump --out {{path/to/directory}}`

- 创建指定数据库的转储：

`mongodump --db {{database_name}}`

- 创建指定数据库中指定集合的转储：

`mongodump --collection {{collection_name}} --db {{database_name}}`

- 连接到运行在指定端口上的指定主机，并创建转储：

`mongodump --host {{host}} --port {{port}}`

- 使用给定用户名创建指定数据库的转储；用户将被提示输入密码：

`mongodump --username {{username}} {{database}} --password`

- 从特定实例创建转储；主机、用户、密码和数据库将在连接字符串中定义：

`mongodump --uri {{connection_string}}`