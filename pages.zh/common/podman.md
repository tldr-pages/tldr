# podman

> 简单的管理工具，用于管理 Pod、容器和镜像。
> Podman 提供了与 Docker-CLI 类似的命令行。简单来说：`alias docker=podman`。
> 更多信息：<https://github.com/containers/podman/blob/main/commands-demo.md>。

- 列出所有容器（包括运行中和已停止的）：

`podman ps --all`

- 从镜像创建一个容器，并指定自定义名称：

`podman run --name {{container_name}} {{image}}`

- 启动或停止一个已存在的容器：

`podman {{start|stop}} {{container_name}}`

- 从镜像仓库拉取镜像（默认为 Docker Hub）：

`podman pull {{image}}`

- 显示已下载的镜像列表：

`podman images`

- 在已运行的容器中打开一个 shell：

`podman exec --interactive --tty {{container_name}} {{sh}}`

- 删除一个已停止的容器：

`podman rm {{container_name}}`

- 显示一个或多个容器的日志并实时跟踪日志输出：

`podman logs --follow {{container_name}} {{container_id}}`