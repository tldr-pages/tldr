# docker pull

> 从注册表下载 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/pull/>.

- 下载特定的 Docker 镜像：

`docker pull {{image}}:{{tag}}`

- 以静默模式下载特定的 Docker 镜像：

`docker pull {{[-q|--quiet]}} {{image}}:{{tag}}`

- 下载特定 Docker 镜像的所有标签：

`docker pull {{[-a|--all-tags]}} {{image}}`

- 下载特定平台的 Docker 镜像，例如：linux/amd64：

`docker pull --platform {{linux/amd64}} {{image}}:{{tag}}`

- 显示帮助：

`docker pull {{[-h|--help]}}`