# cypher-shell

> 打开一个交互式会话，并对 Neo4j 实例运行 Cypher 查询。
> 参见：`neo4j-admin`，`mysql`。
> 更多信息：<https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>。

- 连接到本地实例的默认端口（`neo4j://localhost:7687`）：

`cypher-shell`

- 连接到远程实例：

`cypher-shell --address neo4j://{{host}}:{{port}}`

- 连接并提供安全凭证：

`cypher-shell --username {{username}} --password {{password}}`

- 连接到特定数据库：

`cypher-shell --database {{database_name}}`

- 执行 Cypher 语句文件并关闭：

`cypher-shell --file {{path/to/file.cypher}}`

- 启用日志记录到文件：

`cypher-shell --log {{path/to/file.log}}`

- 显示帮助：

`cypher-shell --help`