# docker 日志

> 打印容器日志。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/logs/>.

- 打印容器的日志：

`docker logs {{container_name}}`

- 打印日志并跟随：

`docker logs -f {{container_name}}`

- 打印最后 5 行：

`docker logs {{container_name}} --tail {{5}}`

- 打印带有时间戳的日志：

`docker logs -t {{container_name}}`

- 打印从容器执行的某个时间点开始的日志（例如 23m，10s，2013-01-02T13:23:37）：

`docker logs {{container_name}} --until {{time}}`