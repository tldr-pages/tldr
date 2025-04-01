# docker network

> 创建和管理 Docker 网络。
> 更多信息：<https://docs.docker.com/reference/cli/docker/network/>.

- 列出 Docker 守护进程上所有可用和已配置的网络：

`docker network ls`

- 创建一个用户定义的网络：

`docker network create --driver {{driver_name}} {{network_name}}`

- 显示一个或多个网络的详细信息：

`docker network inspect {{network_name1 network_name2 ...}}`

- 使用名称或 ID 将容器连接到网络：

`docker network connect {{network_name}} {{container_name|ID}}`

- 将容器从网络断开连接：

`docker network disconnect {{network_name}} {{container_name|ID}}`

- 删除所有未使用的（未被任何容器引用的）网络：

`docker network prune`

- 删除一个或多个未使用的网络：

`docker network rm {{network_name1 network_name2 ...}}`