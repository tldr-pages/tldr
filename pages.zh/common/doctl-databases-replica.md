# doctl databases replica

> 管理与数据库集群关联的只读副本。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- 使用访问令牌运行 `doctl databases replica` 命令:

`doctl databases pool {{command}} --access-token {{access_token}}`

- 获取只读数据库副本的信息:

`doctl databases replica get {{database_id}} {{replica_name}}`

- 获取只读数据库副本的列表:

`doctl databases replica list {{database_id}}`

- 创建只读数据库副本:

`doctl databases replica create {{database_id}} {{replica_name}}`

- 删除只读数据库副本:

`doctl databases replica delete {{database_id}} {{replica_name}}`
