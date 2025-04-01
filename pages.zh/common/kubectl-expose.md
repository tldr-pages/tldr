# kubectl expose

> 将资源暴露为新的 Kubernetes 服务。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose>.

- 为资源创建一个服务，该服务将从容器端口提供到节点端口：

`kubectl expose {{resource_type}} {{resource_name}} --port={{node_port}} --target-port={{container_port}}`

- 为通过文件标识的资源创建一个服务：

`kubectl expose -f {{path/to/file.yml}} --port={{node_port}} --target-port={{container_port}}`

- 为资源创建一个命名服务，该服务将使用相同的端口从节点到容器提供：

`kubectl expose {{resource_type}} {{resource_name}} --port={{node_port}} --name={{service_name}}`