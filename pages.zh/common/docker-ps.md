# docker ps

> 列出 Docker 容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/ls/>。

- 列出当前正在运行的 Docker 容器：

`docker ps`

- 列出所有 Docker 容器（包括运行中和已停止的）：

`docker ps {{[-a|--all]}}`

- 显示最新创建的容器（包括所有状态）：

`docker ps {{[-l|--latest]}}`

- 过滤名称中包含特定子字符串的容器：

`docker ps {{[-f|--filter]}} "name={{name}}"`

- 过滤具有指定镜像作为祖先的容器：

`docker ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- 按退出状态码过滤容器：

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- 按状态过滤容器（创建、运行中、移除中、暂停、已退出和已死亡）：

`docker ps {{[-f|--filter]}} "status={{status}}"`

- 过滤挂载了特定卷或在特定路径下有卷挂载的容器：

`docker ps {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`