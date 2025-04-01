# doctl databases user

> 查看和创建数据库用户。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/user>.

- 使用访问令牌执行 `doctl databases user` 命令：

`doctl databases user {{command}} --access-token {{access_token}}`

- 获取数据库用户的详细信息：

`doctl databases user get {{database_id}} {{user_name}}`

- 获取指定数据库的用户列表：

`doctl databases user list {{database_id}}`

- 重置指定用户的认证密码：

`doctl databases user reset {{database_id}} {{user_name}}`

- 重置指定用户的 MySQL 认证插件：

`doctl databases user reset {{database_id}} {{user_name}} {{caching_sha2_password|mysql_native_password}}`

- 在指定的数据库中创建一个指定用户名的用户：

`doctl databases user create {{database_id}} {{user_name}}`

- 从指定的数据库中删除一个指定用户名的用户：

`doctl databases user delete {{database_id}} {{user_name}}`