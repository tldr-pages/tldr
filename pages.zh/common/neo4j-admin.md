# neo4j-admin

> 管理和管理 Neo4j 数据库管理系统 (DBMS)。
> 另见: `cypher-shell`, `mysqld`。
> 更多信息: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- 启动 DBMS:

`neo4j-admin server start`

- 停止 DBMS:

`neo4j-admin server stop`

- 设置默认 `neo4j` 用户的初始密码（这是第一次启动 DBMS 的前提）:

`neo4j-admin dbms set-initial-password {{database_name}}`

- 将离线数据库的存档（转储）创建为名为 `database_name.dump` 的文件:

`neo4j-admin database dump --to-path={{path/to/directory}} {{database_name}}`

- 从名为 `database_name.dump` 的存档加载数据库:

`neo4j-admin database load --from-path={{path/to/directory}} {{database_name}} --overwrite-destination=true`

- 通过 `stdin` 从指定的存档文件加载数据库:

`neo4j-admin database load --from-stdin {{database_name}} --overwrite-destination=true < {{path/to/filename.dump}}`

- 显示帮助:

`neo4j-admin --help`