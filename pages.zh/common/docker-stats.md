# docker stats

> 显示容器的资源使用统计信息的实时流。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/stats/>.

- 显示所有正在运行的容器的统计信息实时流：

`docker stats`

- 显示一个或多个容器的统计信息实时流：

`docker stats {{container1 container2 ...}}`

- 更改列格式以显示容器的 CPU 使用百分比：

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- 显示所有容器（包括正在运行和已停止的）的统计信息：

`docker stats --all`

- 禁用流式统计，仅提取当前统计信息：

`docker stats --no-stream`