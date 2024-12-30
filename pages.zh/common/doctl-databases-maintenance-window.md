# doctl 数据库维护窗口

> 为您的数据库安排和检查维护窗口的时间表。
> 更多信息: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>。

- 使用访问令牌运行 `doctl databases maintenance-window` 命令：

`doctl databases maintenance-window {{command}} --access-token {{access_token}}`

- 检索数据库集群维护窗口的详细信息：

`doctl databases maintenance-window get {{database_id}}`

- 更新数据库集群的维护窗口：

`doctl databases maintenance-window update {{database_id}} --day {{day_of_the_week}} --hour {{hour_in_24_hours_format}}`