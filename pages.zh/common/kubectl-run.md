# kubectl run

> 在 Kubernetes 中运行 Pod。指定 Pod 生成器以在某些 K8S 版本中避免弃用错误。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- 运行一个 nginx Pod 并暴露 80 端口：

`kubectl run {{nginx-dev}} --image=nginx --port 80`

- 运行一个 nginx Pod，并设置环境变量 TEST_VAR：

`kubectl run {{nginx-dev}} --image=nginx --env="{{TEST_VAR}}={{testing}}"`

- 显示创建 nginx 容器时将进行的 API 调用：

`kubectl run {{nginx-dev}} --image=nginx --dry-run={{none|server|client}}`

- 以交互方式运行一个 Ubuntu Pod，从不重启它，并在退出时删除：

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- 运行一个 Ubuntu Pod，覆盖默认命令为 echo，并指定自定义参数：

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --command -- echo {{argument1 argument2 ...}}`
