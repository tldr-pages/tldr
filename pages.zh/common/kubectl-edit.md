# kubectl edit

> 编辑 Kubernetes 资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#edit>。

- 编辑一个 Pod:

`kubectl edit pod/{{pod_name}}`

- 编辑一个 Deployment:

`kubectl edit deployment/{{deployment_name}}`

- 编辑一个 Service:

`kubectl edit svc/{{service_name}}`

- 使用特定的编辑器编辑资源:

`KUBE_EDITOR={{nano}} kubectl edit {{resource}}/{{resource_name}}`

- 以 JSON 格式编辑资源:

`kubectl edit {{resource}}/{{resource_name}} --output json`
