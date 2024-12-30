# docker build

> 从 Dockerfile 构建一个镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/buildx/build/>。

- 使用当前目录中的 Dockerfile 构建一个 Docker 镜像：

`docker build .`

- 从指定 URL 的 Dockerfile 构建一个 Docker 镜像：

`docker build {{github.com/creack/docker-firefox}}`

- 构建一个 Docker 镜像并为其打标签：

`docker build --tag {{name:tag}} .`

- 在没有构建上下文的情况下构建 Docker 镜像：

`docker build --tag {{name:tag}} - < {{Dockerfile}}`

- 在构建镜像时不使用缓存：

`docker build --no-cache --tag {{name:tag}} .`

- 使用特定的 Dockerfile 构建 Docker 镜像：

`docker build --file {{Dockerfile}} .`

- 使用自定义构建时变量进行构建：

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`