# sqsc

> 命令行 AWS Simple Queue Service 客户端。
> 更多信息：<https://github.com/yongfei25/sqsc>。

- 列出所有队列：

`sqsc lq {{queue_prefix}}`

- 列出队列中的所有消息：

`sqsc ls {{queue_name}}`

- 将一个队列中的所有消息复制到另一个队列：

`sqsc cp {{source_queue}} {{destination_queue}}`

- 将一个队列中的所有消息移动到另一个队列：

`sqsc mv {{source_queue}} {{destination_queue}}`

- 描述一个队列：

`sqsc describe {{queue_name}}`

- 使用 SQL 语法查询队列：

`sqsc query "SELECT body FROM {{queue_name}} WHERE body LIKE '%user%'"`

- 将队列中的所有消息拉取到当前工作目录中的本地 SQLite 数据库：

`sqsc pull {{queue_name}}`
