# podman rmi

> 移除 Podman 镜像。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>。

- 根据名称移除一个或多个镜像：

`podman rmi {{image:tag}} {{image2:tag}} {{...}}`

- 强制移除一个镜像：

`podman rmi --force {{image}}`

- 移除一个镜像而不删除未标记的父镜像：

`podman rmi --no-prune {{image}}`

- 显示帮助信息：

`podman rmi`