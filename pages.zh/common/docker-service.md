# docker service

> 管理 Docker 守护程序上的服务。
> 更多信息：<https://docs.docker.com/reference/cli/docker/service/>.

- 列出 Docker 守护程序上的服务：

`docker service ls`

- 创建一个新的服务：

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- 显示一个或多个服务的详细信息：

`docker service inspect {{service_name_or_ID1 service_name_or_ID2}}`

- 列出一个或多个服务的任务：

`docker service ps {{service_name_or_ID1 service_name_or_ID2 ...}}`

- 将一个以空格分隔的服务列表扩展到特定数量的副本：

`docker service scale {{service_name}}={{count_of_replicas}}`

- 移除一个或多个服务：

`docker service rm {{service_name_or_ID1 service_name_or_ID2}}`