# mongodump

> 用于导出 MongoDB 实例的内容。
> 更多信息：<https://docs.mongodb.com/database-tools/mongodump/>。

- 导出所有数据库的内容（这将把文件放在一个名为“dump”的目录中）：

`mongodump`

- 指定导出文件的存储位置：

`mongodump --out {{path/to/directory}}`

- 导出指定数据库的内容：

`mongodump --db {{database_name}}`

- 导出指定数据库中的指定集合：

`mongodump --collection {{collection_name}} --db {{database_name}}`

- 连接到指定主机和端口上的 MongoDB 实例并导出数据：

`mongodump --host {{host}} --port {{port}}`

- 使用给定的用户名导出指定数据库的内容；用户将被提示输入密码：

`mongodump --username {{username}} {{database}} --password`

- 从特定实例中导出数据；主机、用户、密码和数据库将在连接字符串中定义：

`mongodump --uri {{connection_string}}`