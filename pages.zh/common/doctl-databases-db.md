# doctl 数据库 db

> 管理由数据库集群提供的数据库。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/db>。

- 使用访问令牌运行 `doctl databases db` 命令：

`doctl databases db {{command}} --access-token {{access_token}}`

- 检索在给定数据库集群中托管的特定数据库的名称：

`doctl databases db get {{database_id}} {{database_name}}`

- 列出在给定数据库集群中托管的现有数据库：

`doctl databases db list {{database_id}}`

- 在给定数据库集群中创建具有给定名称的数据库：

`doctl databases db create {{database_id}} {{database_name}}`

- 删除在给定数据库集群中具有给定名称的数据库：

`doctl databases db delete {{database_id}} {{database_name}}`