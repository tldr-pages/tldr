# redis-cli

> 打开与 Redis 服务器的连接。
> 更多信息：<https://redis.io/topics/rediscli>。

- 连接到本地服务器：

`redis-cli`

- 连接到默认端口（6379）的远程服务器：

`redis-cli -h {{host}}`

- 连接到指定端口号的远程服务器：

`redis-cli -h {{host}} -p {{port}}`

- 使用 URI 连接到远程服务器：

`redis-cli -u {{uri}}`

- 指定密码：

`redis-cli -a {{password}}`

- 执行 Redis 命令：

`redis-cli {{redis_command}}`

- 连接到本地集群：

`redis-cli -c`