# docker compose logs

> 查看 Docker Compose 应用中各容器的日志输出。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/logs/>。

- 查看所有服务的日志：

`docker compose logs`

- 查看指定服务的日志：

`docker compose logs {{服务名}}`

- 查看日志并持续跟踪新输出（类似 `tail --follow`）：

`docker compose logs {{[-f|--follow]}}`

- 查看带时间戳的日志：

`docker compose logs {{[-t|--timestamps]}}`

- 仅查看每个容器最近 `n` 行日志：

`docker compose logs {{[-n|--tail]}} {{n}}`

- 查看从指定时间开始的日志：

`docker compose logs --since {{时间戳}}`

- 查看截至指定时间的日志：

`docker compose logs --until {{时间戳}}`

- 查看多个指定服务的日志：

`docker compose logs {{服务1 服务2 ...}}`
