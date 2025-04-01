# doctl databases firewalls

> 管理数据库集群的防火墙。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls>.

- 使用访问令牌运行 `doctl databases firewalls` 命令：

`doctl databases firewalls {{command}} --access-token {{access_token}}`

- 获取指定数据库的防火墙规则列表：

`doctl databases firewalls list`

- 为指定数据库添加防火墙规则：

`doctl databases firewalls append {{database_id}} --rule {{droplet|k8s|ip_addr|tag|app}}:{{value}}`

- 为指定数据库删除防火墙规则：

`doctl databases firewalls remove {{database_id}} {{rule_uuid}}`