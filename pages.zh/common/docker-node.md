# docker 节点

> 管理 Docker Swarm 节点。
> 更多信息：<https://docs.docker.com/reference/cli/docker/node/>.

- 列出 swarm 中的节点：

`docker node ls`

- 列出一个或多个节点上运行的任务，默认是当前节点：

`docker node ps {{node1 node2 node3 ...}}`

- 显示一个或多个节点的详细信息：

`docker node inspect {{node1 node2 node3 ...}}`

- 将一个或多个节点提升为 swarm 中的管理者：

`docker node promote {{node1 node2 node3 ...}}`

- 将一个或多个节点降级为 swarm 中的管理者：

`docker node demote {{node1 node2 node3 ...}}`

- 从 swarm 中删除一个或多个节点：

`docker node rm {{node1 node2 node3 ...}}`

- 更新节点的元数据，例如其可用性、标签或角色：

`docker node update --{{availability|role|label-add|...}} {{active|worker|foo|...}} {{node1}}`