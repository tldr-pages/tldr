# docker 系统

> 管理 Docker 数据并显示系统范围的信息。
> 更多信息：<https://docs.docker.com/reference/cli/docker/system/>。

- 显示帮助：

`docker system`

- 显示 Docker 磁盘使用情况：

`docker system df`

- 显示磁盘使用的详细信息：

`docker system df --verbose`

- 删除未使用的数据：

`docker system prune`

- 删除指定时间之前创建的未使用数据：

`docker system prune --filter "until={{hours}}h{{minutes}}m"`

- 显示来自 Docker 守护进程的实时事件：

`docker system events`

- 显示以有效 JSON Lines 格式流式传输的容器的实时事件：

`docker system events --filter 'type=container' --format '{{json .}}'`

- 显示系统范围的信息：

`docker system info`