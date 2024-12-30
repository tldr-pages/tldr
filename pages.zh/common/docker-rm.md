# docker rm

> 删除容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/rm/>.

- 删除容器：

`docker rm {{container1 container2 ...}}`

- 强制删除一个容器：

`docker rm --force {{container1 container2 ...}}`

- 删除一个容器及其卷：

`docker rm --volumes {{container}}`

- 显示帮助：

`docker rm --help`