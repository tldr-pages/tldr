# aws eks

> 管理 Amazon Elastic Kubernetes Service（EKS）的插件、集群和节点组。
> Amazon EKS 是一种用于在 AWS 上轻松运行 Kubernetes 的服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/eks/>.

- 创建一个 EKS 集群：

`aws eks create-cluster --name {{集群名称}} --role-arn {{eks_服务角色_arn}} --resources-vpc-config subnetIds={{子网_ID_列表}},securityGroupIds={{安全组_ID_列表}}`

- 更新 kubeconfig 以连接到 EKS 集群：

`aws eks update-kubeconfig --name {{集群名称}}`

- 列出可用的 EKS 集群：

`aws eks list-clusters`

- 查看 EKS 集群的详细信息：

`aws eks describe-cluster --name {{集群名称}}`

- 删除一个 EKS 集群：

`aws eks delete-cluster --name {{集群名称}}`

- 列出 EKS 集群中的节点组：

`aws eks list-nodegroups --cluster-name {{集群名称}}`

- 查看节点组的详细信息：

`aws eks describe-nodegroup --cluster-name {{集群名称}} --nodegroup-name {{节点组名称}}`
