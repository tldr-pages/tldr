# redis-server

> 持久化键值数据库。
> 更多信息：<https://redis.io>。

- 启动 Redis 服务器，使用默认端口（6379），并将日志写入 `stdout`：

`redis-server`

- 启动 Redis 服务器，使用默认端口，作为后台进程：

`redis-server --daemonize yes`

- 启动 Redis 服务器，使用指定端口，作为后台进程：

`redis-server --port {{port}} --daemonize yes`

- 使用自定义配置文件启动 Redis 服务器：

`redis-server {{path/to/redis.conf}}`

- 启动 Redis 服务器并启用详细日志记录：

`redis-server --loglevel {{warning|notice|verbose|debug}}`