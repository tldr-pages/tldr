# docker image

> 管理 Docker 镜像。
> 参见：`docker build`, `docker import` 和 `docker pull`。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/>。

- 列出本地 Docker 镜像：

`docker image ls`

- 删除未使用的本地 Docker 镜像：

`docker image prune`

- 删除所有未使用的镜像（不仅仅是没有标签的）：

`docker image prune --all`

- 显示本地 Docker 镜像的历史：

`docker image history {{image}}`

- 查看 `docker image rm` 的文档：

`tldr docker rmi`
