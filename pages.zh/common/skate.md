# skate

> 简单而强大的键值存储工具。
> 更多信息：<https://github.com/charmbracelet/skate>.

- 在默认数据库中存储一个键和一个值：

`skate set "{{key}}" "{{value}}"`

- 显示默认数据库中保存的键：

`skate list`

- 从默认数据库中删除键和值：

`skate delete "{{key}}"`

- 在新数据库中创建一个新的键和值：

`skate set "{{key}}"@"{{database_name}}" "{{value}}"`

- 显示非默认数据库中保存的键：

`skate list @"{{database_name}}"`

- 从特定数据库中删除键和值：

`skate delete "{{key}}"@"{{database_name}}"`

- 显示可用的数据库：

`skate list-dbs`

- 删除本地数据库并从 Charm Cloud 拉取最新副本：

`skate reset @"{{database_name}}"`