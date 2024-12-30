# docker ps

> 列出 Docker 容器。
> 更多信息: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- 列出当前正在运行的 Docker 容器：

`docker ps`

- 列出所有 Docker 容器（运行中和已停止的）：

`docker ps --all`

- 显示最新创建的容器（包括所有状态）：

`docker ps --latest`

- 过滤名称中包含子字符串的容器：

`docker ps --filter "name={{name}}"`

- 过滤共享给定镜像作为祖先的容器：

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- 按退出状态码过滤容器：

`docker ps --all --filter "exited={{code}}"`

- 按状态过滤容器（创建、运行、删除、暂停、退出和死亡）：

`docker ps --filter "status={{status}}"`

- 过滤挂载特定卷或在特定路径下挂载卷的容器：

`docker ps --filter "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`