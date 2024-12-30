# docker compose

> 运行和管理多容器的Docker应用程序。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/>。

- 列出所有正在运行的容器：

`docker compose ps`

- 使用当前目录中的 `docker-compose.yml` 文件在后台创建并启动所有容器：

`docker compose up --detach`

- 启动所有容器，如有必要则重建：

`docker compose up --build`

- 通过指定项目名称和使用不同的 Compose 文件启动所有容器：

`docker compose -p {{project_name}} --file {{path/to/file}} up`

- 停止所有正在运行的容器：

`docker compose stop`

- 停止并删除所有容器、网络、镜像和卷：

`docker compose down --rmi all --volumes`

- 跟踪所有容器的日志：

`docker compose logs --follow`

- 跟踪特定容器的日志：

`docker compose logs --follow {{container_name}}`