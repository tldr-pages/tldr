# doctl databases options

> 查看每个数据库引擎下的可用选项。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/options>.

- 使用访问令牌运行 `doctl databases options` 命令：

`doctl databases options {{command}} --access-token {{access_token}}`

- 获取可用数据库引擎的列表：

`doctl databases options engines`

- 获取特定数据库引擎的可用区域列表：

`doctl databases options regions --engine {{pg|mysql|redis|mongodb}}`

- 获取特定数据库引擎的可用大小标识（slugs）列表：

`doctl databases options slugs --engine {{pg|mysql|redis|mongodb}}`

- 获取特定数据库引擎的可用版本列表：

`doctl databases options versions --engine {{pg|mysql|redis|mongodb}}`