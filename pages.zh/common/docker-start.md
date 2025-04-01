# docker start

> 启动已停止的容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/start/>.

- 显示帮助：

`docker start --help`

- 启动一个 Docker 容器：

`docker start {{container}}`

- 启动一个容器，附加 `stdout` 和 `stderr` 并转发信号：

`docker start {{[-a|--attach]}} {{container}}`

- 启动一个或多个容器：

`docker start {{container1 container2 ...}}`