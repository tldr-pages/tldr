# docker swarm

> 容器编排工具。
> 更多信息：<https://docs.docker.com/engine/swarm/>。

- 初始化一个 Swarm 集群：

`docker swarm init`

- 显示加入管理节点或工作节点的 token：

`docker swarm join-token {{worker|manager}}`

- 将新节点加入集群：

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- 从 Swarm 中移除一个工作节点（在工作节点内运行）：

`docker swarm leave`

- 显示当前的 CA 证书（PEM 格式）：

`docker swarm ca`

- 旋转当前的 CA 证书并显示新的证书：

`docker swarm ca --rotate`

- 更改节点证书的有效期：

`docker swarm update --cert-expiry {{hours}}h{{minutes}}m{{seconds}}s`
