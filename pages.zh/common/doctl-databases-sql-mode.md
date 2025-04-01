# doctl databases sql-mode

> 查看和配置 MySQL 数据库集群的全局 SQL 模式。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- 使用访问令牌运行 `doctl databases sql-mode` 命令：

`doctl databases sql-mode {{command}} --access-token {{access_token}}`

- 获取 MySQL 数据库集群的 SQL 模式：

`doctl databases sql-mode get {{database_id}}`

- 将 MySQL 数据库集群的 SQL 模式设置为指定模式：

`doctl databases sql-mode set {{database_id}} {{sql_mode_1 sql_mode_2 ...}}`