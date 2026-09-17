# docker compose up

> 启动并运行 Compose 文件中定义的 Docker 服务。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/up/>。

- 启动 docker-compose 文件中定义的所有服务：

`docker compose up`

- 在后台启动服务（分离模式）：

`docker compose up {{[-d|--detach]}}`

- 启动服务前重新构建镜像：

`docker compose up --build`

- 仅启动指定服务：

`docker compose up {{服务1 服务2 ...}}`

- 使用自定义 compose 文件启动服务：

`docker compose {{[-f|--file]}} {{路径/到/配置文件}} up`

- 启动服务并删除孤立容器：

`docker compose up --remove-orphans`

- 启动服务并指定实例数量：

`docker compose up --scale {{服务}}={{数量}}`

- 启动服务并在日志中显示时间戳：

`docker compose up --timestamps`
