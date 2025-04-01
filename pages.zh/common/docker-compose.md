# docker compose

> 运行和管理多容器 Docker 应用程序。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/>.

- 列出所有运行中的容器：

`docker compose ps`

- 从当前目录的 `docker-compose.yml` 文件创建并启动所有容器，并在后台运行：

`docker compose up --detach`

- 启动所有容器，必要时重新构建：

`docker compose up --build`

- 指定项目名称并使用替代的编排文件启动所有容器：

`docker compose -p {{project_name}} --file {{path/to/file}} up`

- 停止所有运行中的容器：

`docker compose stop`

- 停止并删除所有容器、网络、镜像和卷：

`docker compose down --rmi all --volumes`

- 跟踪所有容器的日志：

`docker compose logs --follow`

- 跟踪特定容器的日志：

`docker compose logs --follow {{container_name}}`
