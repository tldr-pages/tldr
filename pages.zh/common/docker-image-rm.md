# docker image rm

> 移除 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/rm/>。

- 根据名称移除一个或多个镜像：

`docker {{[rmi|image rm]}} {{镜像1 镜像2 ...}}`

- 强制移除镜像：

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{镜像}}`

- 移除镜像但不删除未标记的父镜像：

`docker {{[rmi|image rm]}} --no-prune {{镜像}}`

- 显示帮助：

`docker {{[rmi|image rm]}} --help`
