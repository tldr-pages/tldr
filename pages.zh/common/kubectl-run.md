# kubectl run

> 在Kubernetes中运行Pod。指定Pod生成器以避免某些K8S版本中的弃用错误。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>。

- 运行一个nginx Pod并暴露80端口：

`kubectl run {{nginx-dev}} --image=nginx --port 80`

- 运行一个nginx Pod，设置TEST_VAR环境变量：

`kubectl run {{nginx-dev}} --image=nginx --env="{{TEST_VAR}}={{testing}}"`

- 显示创建nginx容器所需的API调用：

`kubectl run {{nginx-dev}} --image=nginx --dry-run={{none|server|client}}`

- 以交互方式运行一个Ubuntu Pod，永不重启，并在退出时将其删除：

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- 运行一个Ubuntu Pod，用echo覆盖默认命令，并指定自定义参数：

`kubectl run {{temp-ubuntu}} --image=ubuntu:22.04 --command -- echo {{argument1 argument2 ...}}`