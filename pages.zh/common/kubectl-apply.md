# kubectl apply

> 通过定义Kubernetes资源的文件管理应用程序。
> 在集群中创建和更新资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>。

- 通过文件名或 `stdin` 将配置应用于资源：

`kubectl apply -f {{resource_filename}}`

- 从默认编辑器编辑资源的最新 last-applied-configuration 注释：

`kubectl apply edit-last-applied -f {{resource_filename}}`

- 通过将其设置为与文件内容匹配来设置最新的 last-applied-configuration 注释：

`kubectl apply set-last-applied -f {{resource_filename}}`

- 通过类型/名称或文件查看最新的 last-applied-configuration 注释：

`kubectl apply view-last-applied -f {{resource_filename}}`