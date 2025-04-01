# podman build

> 用于构建容器镜像的无守护进程工具。
> Podman 提供了类似于 Docker-CLI 的命令行工具。简单来说：`alias docker=podman`。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-build.1.html>。

- 使用指定目录中的 `Dockerfile` 或 `Containerfile` 创建镜像：

`podman build {{path/to/directory}}`

- 创建带有指定标签的镜像：

`podman build --tag {{image_name:version}} {{path/to/directory}}`

- 从非标准文件创建镜像：

`podman build --file {{Containerfile.different}} .`

- 创建镜像时不使用任何缓存的镜像：

`podman build --no-cache {{path/to/directory}}`

- 创建镜像时抑制所有输出：

`podman build --quiet {{path/to/directory}}`
