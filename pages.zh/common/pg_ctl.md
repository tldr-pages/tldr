# pg_ctl

> 用于控制 PostgreSQL 服务器和数据库集群的工具。
> 更多信息：<https://www.postgresql.org/docs/current/app-pg-ctl.html>。

- 初始化一个新的 PostgreSQL 数据库集群：

`pg_ctl -D {{data_directory}} init`

- 启动 PostgreSQL 服务器：

`pg_ctl -D {{data_directory}} start`

- 停止 PostgreSQL 服务器：

`pg_ctl -D {{data_directory}} stop`

- 重启 PostgreSQL 服务器：

`pg_ctl -D {{data_directory}} restart`

- 重新加载 PostgreSQL 服务器配置：

`pg_ctl -D {{data_directory}} reload`
