# podman ps

> 列出 Podman 容器。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-ps.1.html>。

- 列出当前正在运行的 Podman 容器：

`podman ps`

- 列出所有 Podman 容器（运行中和已停止）：

`podman ps --all`

- 显示最新创建的容器（包括所有状态）：

`podman ps --latest`

- 过滤包含指定子字符串的容器名称：

`podman ps --filter "name={{name}}"`

- 过滤共享指定镜像作为祖先的容器：

`podman ps --filter "ancestor={{image}}:{{tag}}"`

- 按退出状态码过滤容器：

`podman ps --all --filter "exited={{code}}"`

- 按状态过滤容器（已创建、运行中、正在删除、暂停、已退出和已死亡）：

`podman ps --filter "status={{status}}"`

- 过滤挂载特定卷或在特定路径中挂载卷的容器：

`podman ps --filter "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`