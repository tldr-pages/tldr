# docker-machine

> 创建和管理运行 Docker 的机器。
> 更多信息：<https://github.com/docker/machine>.

- 列出当前正在运行的 Docker 机器：

`docker-machine ls`

- 使用特定名称创建新的 Docker 机器：

`docker-machine create {{name}}`

- 获取机器的状态：

`docker-machine status {{name}}`

- 启动机器：

`docker-machine start {{name}}`

- 停止机器：

`docker-machine stop {{name}}`

- 查看机器的详细信息：

`docker-machine inspect {{name}}`