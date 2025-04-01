# doctl databases maintenance-window

> 安排和查看数据库的维护窗口。
> 更多信息： <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>.

- 使用访问令牌运行 `doctl databases maintenance-window` 命令:

`doctl databases maintenance-window {{command}} --access-token {{access_token}}`

- 获取数据库集群的维护窗口详情:

`doctl databases maintenance-window get {{database_id}}`

- 更新数据库集群的维护窗口:

`doctl databases maintenance-window update {{database_id}} --day {{day_of_the_week}} --hour {{hour_in_24_hours_format}}`
