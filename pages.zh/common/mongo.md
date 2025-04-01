# mongo

> 旧版 MongoDB 命令行工具。请参阅 `mongosh` 以获取新版命令行工具。
> 注意：所有连接选项可以用一个字符串替换：`mongodb://user@host:port/db_name?authSource=authdb_name`。
> 更多信息：<https://docs.mongodb.com/manual/reference/program/mongo>。

- 连接到默认端口（`mongodb://localhost:27017`）上的本地数据库：

`mongo`

- 连接到指定的数据库：

`mongo --host {{host}} --port {{port}} {{db_name}}`

- 使用指定的用户名在指定的数据库上进行身份验证（将提示输入密码）：

`mongo --host {{host}} --port {{port}} --username {{username}} --authenticationDatabase {{authdb_name}} {{db_name}}`

- 在数据库上评估 JavaScript 表达式：

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{db_name}}`