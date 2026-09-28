# docker image load

> 从文件或 `stdin` 加载 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/load/>。

- 从 `stdin` 加载 Docker 镜像：

`docker < {{路径/到/镜像文件.tar}} {{[load|image load]}}`

- 从指定文件加载 Docker 镜像：

`docker {{[load|image load]}} {{[-i|--input]}} {{路径/到/镜像文件.tar}}`

- 以静默模式从指定文件加载 Docker 镜像：

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{路径/到/镜像文件.tar}}`
