# mongosh

> MongoDB的新Shell，替代`mongo`。
> 注意：所有连接选项可以用一个字符串替换：`mongodb://user@host:port/db_name?authSource=authdb_name`。
> 更多信息：<https://www.mongodb.com/docs/mongodb-shell>。

- 连接到本地数据库，默认端口（`mongodb://localhost:27017`）：

`mongosh`

- 连接到数据库：

`mongosh --host {{host}} --port {{port}} {{db_name}}`

- 使用指定的用户名在指定的数据库上进行身份验证（你需要输入密码）：

`mongosh --host {{host}} --port {{port}} --username {{username}} --authenticationDatabase {{authdb_name}} {{db_name}}`

- 在数据库上评估JavaScript表达式：

`mongosh --eval '{{JSON.stringify(db.foo.findOne())}}' {{db_name}}`