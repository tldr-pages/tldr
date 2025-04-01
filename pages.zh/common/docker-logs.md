# docker logs

> 打印容器日志。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/logs/>.

- 打印来自容器的日志：

`docker logs {{container_name}}`

- 打印并跟踪容器日志：

`docker logs {{[-f|--follow]}} {{container_name}}`

- 打印最后 5 行日志：

`docker logs {{container_name}} {{[-n|--tail]}} {{5}}`

- 打印带有时间戳的日志：

`docker logs {{[-t|--timestamps]}} {{container_name}}`

- 从容器执行的某个时间点开始打印日志（例如：23m, 10s, 2013-01-02T13:23:37）：

`docker logs {{container_name}} --until {{time}}`
