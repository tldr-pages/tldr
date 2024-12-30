# minikube

> 在本地运行Kubernetes。
> 更多信息请访问：<https://minikube.sigs.k8s.io/docs/>。

- 启动集群：

`minikube start`

- 获取集群的IP地址：

`minikube ip`

- 访问通过节点端口暴露的名为my_service的服务并获取URL：

`minikube service {{my_service}} --url`

- 在浏览器中打开Kubernetes仪表盘：

`minikube dashboard`

- 停止正在运行的集群：

`minikube stop`

- 删除集群：

`minikube delete`

- 连接到负载均衡器服务：

`minikube tunnel`