# docker pull

> 从注册表下载 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/pull/>。

- 下载特定的 Docker 镜像：

`docker pull {{image}}:{{tag}}`

- 以安静模式下载特定的 Docker 镜像：

`docker pull --quiet {{image}}:{{tag}}`

- 下载特定 Docker 镜像的所有标签：

`docker pull --all-tags {{image}}`

- 为特定平台下载 Docker 镜像，例如 linux/amd64：

`docker pull --platform {{linux/amd64}} {{image}}:{{tag}}`

- 显示帮助：

`docker pull --help`