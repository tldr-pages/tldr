# aws eks

> 管理 Amazon Elastic Kubernetes Service (EKS) 的附加组件、集群和节点组。
> Amazon EKS 是在 AWS 上轻松运行 Kubernetes 的服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html>。

- 创建 EKS 集群：

`aws eks create-cluster --name {{cluster_name}} --role-arn {{eks_service_role_arn}} --resources-vpc-config {{subnetIds={{subnet_ids}},securityGroupIds={{security_group_ids}}}}`

- 更新 kubeconfig 以连接到 EKS 集群：

`aws eks update-kubeconfig --name {{cluster_name}}`

- 列出可用的 EKS 集群：

`aws eks list-clusters`

- 描述 EKS 集群的详细信息：

`aws eks describe-cluster --name {{cluster_name}}`

- 删除 EKS 集群：

`aws eks delete-cluster --name {{cluster_name}}`

- 列出 EKS 集群中的节点组：

`aws eks list-nodegroups --cluster-name {{cluster_name}}`

- 描述节点组的详细信息：

`aws eks describe-nodegroup --cluster-name {{cluster_name}} --nodegroup-name {{nodegroup_name}}`
