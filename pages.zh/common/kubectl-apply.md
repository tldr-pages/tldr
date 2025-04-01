# kubectl apply

> 通过定义 Kubernetes 资源的文件来管理应用程序。
> 在集群中创建和更新资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

- 通过文件名或 `stdin` 将配置应用到资源：

`kubectl apply -f {{resource_filename}}`

- 使用默认编辑器编辑资源的最新 last-applied-configuration 注解：

`kubectl apply edit-last-applied -f {{resource_filename}}`

- 通过将 last-applied-configuration 注解设置为文件内容来更新其值：

`kubectl apply set-last-applied -f {{resource_filename}}`

- 按类型/名称或文件查看最新的 last-applied-configuration 注解：

`kubectl apply view-last-applied -f {{resource_filename}}`
