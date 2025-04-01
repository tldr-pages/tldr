# doctl databases db

> 管理由数据库集群提供的数据库。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/db>。

- 使用访问令牌运行 `doctl databases db` 命令：

`doctl databases db {{command}} --access-token {{access_token}}`

- 获取指定数据库集群中托管的指定数据库的名称：

`doctl databases db get {{database_id}} {{database_name}}`

- 列出指定数据库集群中托管的所有现有数据库：

`doctl databases db list {{database_id}}`

- 在指定的数据库集群中创建一个指定名称的数据库：

`doctl databases db create {{database_id}} {{database_name}}`

- 删除指定数据库集群中指定名称的数据库：

`doctl databases db delete {{database_id}} {{database_name}}`
