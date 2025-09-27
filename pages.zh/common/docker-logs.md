# docker logs

> 显示容器的日志。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/logs/>.

- 显示一个容器的日志：

`docker logs {{容器_名称}}`

- 显示历史日志，然后跟踪容器日志：

`docker logs {{[-f|--follow]}} {{容器_名称}}`

- 显示最后 5 行日志：

`docker logs {{容器_名称}} {{[-n|--tail]}} {{5}}`

- 显示带有时间戳的日志：

`docker logs {{[-t|--timestamps]}} {{容器_名称}}`

- 展示容器运行过程中，自某个时间点以来的日志（也就是，23m、10s、2013-01-02T13:23:37）：

`docker logs {{容器_名称}} --until {{时间点}}`
