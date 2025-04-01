# podman-compose

> 运行和管理 Compose 规范定义的容器。
> 更多信息：<https://github.com/containers/podman-compose>.

- 列出所有正在运行的容器：

`podman-compose ps`

- 使用本地的 `docker-compose.yml` 在后台创建并启动所有容器：

`podman-compose up -d`

- 启动所有容器，必要时进行构建：

`podman-compose up --build`

- 使用其他组合文件启动所有容器：

`podman-compose {{[-f|--file]}} {{path/to/file.yaml}} up`

- 停止所有正在运行的容器：

`podman-compose stop`

- 移除所有容器、网络和卷：

`podman-compose down --volumes`

- 跟踪容器的日志（省略所有容器名称）：

`podman-compose logs --follow {{container_name}}`

- 在服务中运行一次性命令，且不映射端口：

`podman-compose run {{service_name}} {{command}}`