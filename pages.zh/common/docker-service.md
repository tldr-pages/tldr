# docker 服务

> 管理 Docker 守护进程上的服务。
> 更多信息：<https://docs.docker.com/reference/cli/docker/service/>。

- 列出 Docker 守护进程上的服务：

`docker service ls`

- 创建一个新服务：

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- 显示一个或多个服务的详细信息：

`docker service inspect {{service_name_or_ID1 service_name_or_ID2}}`

- 列出一个或多个服务的任务：

`docker service ps {{service_name_or_ID1 service_name_or_ID2 ...}}`

- 将一个用空格分隔的服务列表的副本数量扩展到特定数量：

`docker service scale {{service_name}}={{count_of_replicas}}`

- 删除一个或多个服务：

`docker service rm {{service_name_or_ID1 service_name_or_ID2}}`