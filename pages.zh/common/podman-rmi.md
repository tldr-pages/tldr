# podman rmi

> 删除 Podman 镜像。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- 根据镜像名称删除一个或多个镜像：

`podman rmi {{image:tag}} {{image2:tag}} {{...}}`

- 强制删除镜像：

`podman rmi --force {{image}}`

- 删除镜像但不删除未标记的父镜像：

`podman rmi --no-prune {{image}}`

- 显示帮助：

`podman rmi`