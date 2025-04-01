# doctl databases

> 管理您的 MySQL、Redis、PostgreSQL 和 MongoDB 数据库服务。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases>.

- 使用访问令牌运行 `doctl databases` 命令：

`doctl databases {{command}} --access-token {{access_token}}`

- 获取数据库集群的详细信息：

`doctl databases get`

- 列出您的数据库集群：

`doctl databases list`

- 创建数据库集群：

`doctl databases create {{database_name}}`

- 删除集群：

`doctl databases delete {{database_id}}`