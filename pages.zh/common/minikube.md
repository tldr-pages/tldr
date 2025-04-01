# minikube

> 在本地运行 Kubernetes。
> 更多信息：<https://minikube.sigs.k8s.io/docs/>。

- 启动集群：

`minikube start`

- 获取集群的 IP 地址：

`minikube ip`

- 访问通过节点端口暴露的服务（名为 my_service），并获取其 URL：

`minikube service {{my_service}} --url`

- 在浏览器中打开 Kubernetes 仪表板：

`minikube dashboard`

- 停止正在运行的集群：

`minikube stop`

- 删除集群：

`minikube delete`

- 连接到 LoadBalancer 服务：

`minikube tunnel`
