# mongorestore

> 用于将二进制转储中的集合或数据库导入到MongoDB实例的实用程序。
> 更多信息：<https://docs.mongodb.com/database-tools/mongorestore/>。

- 从目录导入BSON数据转储到MongoDB数据库：

`mongorestore --db {{database_name}} {{path/to/directory}}`

- 从目录导入BSON数据转储到运行在指定端口的MongoDB服务器主机中的指定数据库，并进行用户身份验证（系统将提示用户输入密码）：

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password`

- 从BSON文件导入集合到MongoDB数据库：

`mongorestore --db {{database_name}} {{path/to/file}}`

- 从BSON文件导入集合到运行在指定端口的MongoDB服务器主机中的指定数据库，并进行用户身份验证（系统将提示用户输入密码）：

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`