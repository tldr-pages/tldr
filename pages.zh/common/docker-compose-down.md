# docker compose down

> 停止并移除由 `docker compose up` 创建的容器、网络、镜像和卷。
> 更多信息：<https://docs.docker.com/reference/cli/docker/compose/down/>。

- 停止并移除所有容器和网络：

`docker compose down`

- 停止并移除容器、网络以及服务使用的所有镜像：

`docker compose down --rmi all`

- 停止并移除容器、网络以及没有自定义标签的镜像：

`docker compose down --rmi local`

- 停止并移除容器、网络和所有卷：

`docker compose down {{[-v|--volumes]}}`

- 停止并移除所有资源，包括孤立容器：

`docker compose down --remove-orphans`

- 使用另一个 Compose 文件停止并移除容器：

`docker compose {{[-f|--file]}} {{路径/到/配置文件}} down`

- 使用以秒为单位的自定义超时停止并移除容器：

`docker compose down {{[-t|--timeout]}} {{秒数}}`

- 移除 Compose 文件中未定义的服务所对应的容器：

`docker compose down --remove-orphans {{[-v|--volumes]}}`
