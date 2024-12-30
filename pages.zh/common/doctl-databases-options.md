# doctl 数据库选项

> 启用浏览每个数据库引擎下可用选项的功能。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/databases/options>。

- 使用访问令牌运行 `doctl databases options` 命令：

`doctl databases options {{command}} --access-token {{access_token}}`

- 检索可用数据库引擎的列表：

`doctl databases options engines`

- 检索给定数据库引擎的可用区域列表：

`doctl databases options regions --engine {{pg|mysql|redis|mongodb}}`

- 检索给定数据库引擎的可用 slug 列表：

`doctl databases options slugs --engine {{pg|mysql|redis|mongodb}}`

- 检索给定数据库引擎的可用版本列表：

`doctl databases options versions --engine {{pg|mysql|redis|mongodb}}`