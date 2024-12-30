# pg_isready

> 检查 PostgreSQL 服务器的连接状态。
> 更多信息：<https://www.postgresql.org/docs/current/app-pg-isready.html>。

- 检查连接：

`pg_isready`

- 检查特定主机名和端口的连接：

`pg_isready --host={{hostname}} --port={{port}}`

- 仅在连接失败时显示消息的连接检查：

`pg_isready --quiet`