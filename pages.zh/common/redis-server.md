# redis-server

> 持久化的键值数据库。
> 更多信息：<https://redis.io>。

- 使用默认端口（6379）启动 Redis 服务器，并将日志写入 `stdout`：

`redis-server`

- 使用默认端口作为后台进程启动 Redis 服务器：

`redis-server --daemonize yes`

- 使用指定端口作为后台进程启动 Redis 服务器：

`redis-server --port {{port}} --daemonize yes`

- 使用自定义配置文件启动 Redis 服务器：

`redis-server {{path/to/redis.conf}}`

- 使用详细日志级别启动 Redis 服务器：

`redis-server --loglevel {{warning|notice|verbose|debug}}`
