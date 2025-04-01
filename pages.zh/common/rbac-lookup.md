# rbac-lookup

> 查找 Kubernetes 集群中任何用户、服务账户或组名绑定的角色和集群角色。
> 更多信息：<https://github.com/reactiveops/rbac-lookup>。

- 查看所有 RBAC 绑定：

`rbac-lookup`

- 查看与给定表达式匹配的 RBAC 绑定：

`rbac-lookup {{search_term}}`

- 查看所有 RBAC 绑定及其源角色绑定：

`rbac-lookup -o wide`

- 按主体过滤查看所有 RBAC 绑定：

`rbac-lookup -k {{user|group|serviceaccount}}`

- 查看所有 RBAC 绑定及 IAM 角色（如果您使用的是 GKE）：

`rbac-lookup --gke`
