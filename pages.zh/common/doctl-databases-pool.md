# doctl databases pool

> 管理数据库集群的连接池。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- 使用访问令牌运行 `doctl databases pool` 命令:

`doctl databases pool {{command}} --access-token {{access_token}}`

- 获取数据库连接池的信息:

`doctl databases pool get {{database_id}} {{pool_name}}`

- 列出数据库集群的连接池:

`doctl databases pool list {{database_id}}`

- 为数据库创建连接池:

`doctl databases pool create {{database_id}} {{pool_name}} --db {{new_pool_name}} --size {{pool_size}}`

- 删除数据库的连接池:

`doctl databases pool delete {{database_id}} {{pool_name}}`