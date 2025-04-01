# mongorestore

> 用于从二进制转储文件将集合或数据库导入到 MongoDB 实例中。
> 更多信息：<https://docs.mongodb.com/database-tools/mongorestore/>.

- 从目录中导入 BSON 数据转储到 MongoDB 数据库：

`mongorestore --db {{database_name}} {{path/to/directory}}`

- 从目录中导入 BSON 数据转储到 MongoDB 服务器主机上的指定数据库，指定端口，并使用用户认证（用户将被提示输入密码）：

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password`

- 从 BSON 文件中导入集合到 MongoDB 数据库：

`mongorestore --db {{database_name}} {{path/to/file}}`

- 从 BSON 文件中导入集合到 MongoDB 服务器主机上的指定数据库，指定端口，并使用用户认证（用户将被提示输入密码）：

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`
