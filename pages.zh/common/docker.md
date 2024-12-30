# Docker

> 管理 Docker 容器和镜像。
> 一些子命令如 `run` 有自己的使用文档。
> 更多信息：<https://docs.docker.com/reference/cli/docker/>。

- 列出所有 Docker 容器（运行中和已停止的）：

`docker ps --all`

- 从镜像启动一个自定义名称的容器：

`docker run --name {{container_name}} {{image}}`

- 启动或停止一个已存在的容器：

`docker {{start|stop}} {{container_name}}`

- 从 Docker 注册表中拉取一个镜像：

`docker pull {{image}}`

- 显示已下载镜像的列表：

`docker images`

- 在运行中的容器内打开一个 [i]nteractive [t]ty 终端，使用 Bourne shell (`sh`)：

`docker exec -it {{container_name}} {{sh}}`

- 移除一个已停止的容器：

`docker rm {{container_name}}`

- 获取并跟踪一个容器的日志：

`docker logs -f {{container_name}}`