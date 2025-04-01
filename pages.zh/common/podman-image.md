# podman image

> 管理 Docker 镜像。
> 参见: `podman build`, `podman import`, 和 `podman pull`。
> 更多信息: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- 列出本地的 Docker 镜像：

`podman image ls`

- 删除未使用的本地 Docker 镜像：

`podman image prune`

- 删除所有未使用的镜像（不仅仅是没有标签的镜像）：

`podman image prune --all`

- 显示本地 Docker 镜像的历史记录：

`podman image history {{image}}`
