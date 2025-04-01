# docker load

> 从文件或 `stdin` 加载 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/load/>.

- 从 `stdin` 加载 Docker 镜像：

`docker load < {{path/to/image_file.tar}}`

- 从指定文件加载 Docker 镜像：

`docker load --input {{path/to/image_file.tar}}`

- 在静默模式下从指定文件加载 Docker 镜像：

`docker load --quiet --input {{path/to/image_file.tar}}`
