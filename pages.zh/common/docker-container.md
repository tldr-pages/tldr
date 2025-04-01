# docker container

> 管理 Docker 容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/>.

- 列出当前正在运行的 Docker 容器：

`docker container ls`

- 启动一个或多个已停止的容器：

`docker container start {{container1_name}} {{container2_name}}`

- 终止一个或多个正在运行的容器：

`docker container kill {{container_name}}`

- 停止一个或多个正在运行的容器：

`docker container stop {{container_name}}`

- 暂停一个或多个容器中的所有进程：

`docker container pause {{container_name}}`

- 显示一个或多个容器的详细信息：

`docker container inspect {{container_name}}`

- 将容器的文件系统导出为 tar 归档文件：

`docker container export {{container_name}}`

- 从容器的更改创建一个新的镜像：

`docker container commit {{container_name}}`
