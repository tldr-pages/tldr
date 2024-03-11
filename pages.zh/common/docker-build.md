# docker build

> 从 Dockerfile 打包镜像。
> 更多信息：<https://docs.docker.com/engine/reference/commandline/build/>.

- 使用当前目录下的 Dockerfile 打包一个 Docker 镜像：

`docker build .`

- 从指定 URL 的 Dockerfile 打包 Docker 镜像：

`docker build {{github.com/creack/docker-firefox}}`

- 打包一个 Docker 镜像并指定镜像的标签：

`docker build --tag {{name:tag}} .`

- 打包一个没有上下文的 Docker 镜像：

`docker build --tag {{name:tag}} - < {{Dockerfile}}`

- 打包镜像时不使用缓存：

`docker build --no-cache --tag {{name:tag}} .`

- 使用指定的 Dockerfile 打包一个 Docker 镜像：

`docker build --file {{Dockerfile}} .`

- 传入自定义变量用于打包：

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
