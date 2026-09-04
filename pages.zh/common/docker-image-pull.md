# docker image pull

> 从镜像仓库下载 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/pull/>。

- 下载指定的 Docker 镜像：

`docker {{[pull|image pull]}} {{镜像}}:{{标签}}`

- 以静默模式下载指定的 Docker 镜像：

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{镜像}}:{{标签}}`

- 下载指定 Docker 镜像的所有标签：

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{镜像}}`

- 下载指定平台的 Docker 镜像：

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{镜像}}:{{标签}}`

- 显示帮助：

`docker {{[pull|image pull]}} --help`
