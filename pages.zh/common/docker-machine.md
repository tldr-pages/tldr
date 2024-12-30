# docker-machine

> 创建和管理运行 Docker 的机器。
> 更多信息：<https://github.com/docker/machine>。

- 列出当前运行的 Docker 机器：

`docker-machine ls`

- 创建一个具有特定名称的新 Docker 机器：

`docker-machine create {{name}}`

- 获取机器的状态：

`docker-machine status {{name}}`

- 启动一台机器：

`docker-machine start {{name}}`

- 停止一台机器：

`docker-machine stop {{name}}`

- 检查有关机器的信息：

`docker-machine inspect {{name}}`