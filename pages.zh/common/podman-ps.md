# podman ps

> 列出 Podman 容器。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-ps.1.html>。

- 列出当前正在运行的 Podman 容器：

`podman ps`

- 列出所有 Podman 容器（包括正在运行和已停止的）：

`podman ps --all`

- 显示最新创建的容器（包括所有状态）：

`podman ps --latest`

- 筛选名称中包含特定子字符串的容器：

`podman ps --filter "name={{name}}"`

- 筛选以特定镜像为基础的容器：

`podman ps --filter "ancestor={{image}}:{{tag}}"`

- 按退出状态码筛选容器：

`podman ps --all --filter "exited={{code}}"`

- 按状态筛选容器（已创建、正在运行、正在移除、已暂停、已退出和已死亡）：

`podman ps --filter "status={{status}}"`

- 筛选挂载了特定卷或在特定路径挂载了卷的容器：

`podman ps --filter "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`