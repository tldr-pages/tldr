# docker rmi

> 删除 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/rm/>.

- 显示帮助：

`docker rmi --help`

- 根据镜像名称删除一个或多个镜像：

`docker rmi {{image1 image2 ...}}`

- 强制删除镜像：

`docker rmi --force {{image}}`

- 删除镜像时不删除未标记的父镜像：

`docker rmi --no-prune {{image}}`
