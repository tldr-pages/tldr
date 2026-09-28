# docker container stop

> 停止一个或多个正在运行的容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/stop/>。

- 停止一个 Docker 容器：

`docker {{[stop|container stop]}} {{容器}}`

- 停止容器，并向其发送指定信号：

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{信号}} {{容器}}`

- 停止容器，并在强制终止前等待指定秒数：

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{秒数}} {{容器}}`

- 停止一个或多个容器：

`docker {{[stop|container stop]}} {{容器1 容器2 ...}}`

- 显示帮助：

`docker {{[stop|container stop]}} --help`
