# docker image

> 管理 Docker 镜像。
> 也请参阅：`docker build`, `docker import`, `docker pull`.
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/>.

- 列出本地的 Docker 镜像：

`docker image ls`

- 删除未使用的 Docker 镜像：

`docker image prune`

- 删除全部的未使用镜像（而不仅仅是那些没有打上标签的镜像）：

`docker image prune {{[-a|--all]}}`

- 展示本地 Docker 镜像的历史：

`docker image history {{镜像}}`

- 查看 `docker image rm` 的文档：

`tldr docker rmi`
