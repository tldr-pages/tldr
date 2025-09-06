# docker

> 管理 Docker 容器和镜像。
> 此命令也有关于其子命令的文件，例如：`run`.
> 更多信息：<https://docs.docker.com/reference/cli/docker/>.

- 列出所有 Docker 容器（包括停止的容器）：

`docker ps {{[-a|--all]}}`

- 透过镜像启动容器，并为容器命名：

`docker run --name {{容器名称}} {{镜像}}`

- 启动或停止现有容器：

`docker {{start|stop}} {{容器名称}}`

- 从 Docker registry 中拉取镜像：

`docker pull {{镜像}}`

- 显示已下载的镜像清单：

`docker images`

- 从正在运行的容器内打开一个交互式 ([i]nteractive) 终端 ([t]ty) shell (`sh`)：

`docker exec {{[-it|--interactive --tty]}} {{容器名称}} {{sh}}`

- 删除一个停止的容器：

`docker rm {{容器名称}}`

- 获取并查看容器的日志：

`docker logs {{[-f|--follow]}} {{容器名称}}`
