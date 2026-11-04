# docker compose stop

> 停止正在运行的容器，但不移除它们。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/stop>。

- 停止所有正在运行的服务：

`docker compose stop`

- 停止指定服务：

`docker compose stop {{服务1 服务2 ...}}`

- 使用以秒为单位的自定义关闭超时停止服务：

`docker compose stop {{[-t|--timeout]}} {{秒数}}`

- 停止指定 Compose 文件中定义的服务：

`docker compose {{[-f|--file]}} {{路径/到/配置文件}} stop`

- 模拟运行（显示操作但不执行）：

`docker compose stop --dry-run`

- 使用自定义超时停止指定服务：

`docker compose stop {{[-t|--timeout]}} {{秒数}} {{服务1 服务2 ...}}`
