# doctl 数据库 用户

> 查看数据库用户的详细信息，并创建数据库用户。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/user>。

- 使用访问令牌运行 `doctl databases user` 命令：

`doctl databases user {{command}} --access-token {{access_token}}`

- 获取数据库用户的详细信息：

`doctl databases user get {{database_id}} {{user_name}}`

- 检索给定数据库的数据库用户列表：

`doctl databases user list {{database_id}}`

- 重置给定用户的身份验证密码：

`doctl databases user reset {{database_id}} {{user_name}}`

- 重置给定用户的 MySQL 身份验证插件：

`doctl databases user reset {{database_id}} {{user_name}} {{caching_sha2_password|mysql_native_password}}`

- 在给定数据库中以给定用户名创建用户：

`doctl databases user create {{database_id}} {{user_name}}`

- 从给定数据库中删除具有给定用户名的用户：

`doctl databases user delete {{database_id}} {{user_name}}`