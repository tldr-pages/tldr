# doctl kubernetes cluster

> 管理 Kubernetes 集群并查看与集群相关的配置选项。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- 创建 Kubernetes 集群：

`doctl kubernetes cluster create --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{cluster_name}}`

- 列出所有 Kubernetes 集群：

`doctl kubernetes cluster list`

- 获取并保存 kubeconfig：

`doctl kubernetes cluster kubeconfig save {{cluster_name}}`

- 检查可用的升级：

`doctl kubernetes cluster get-upgrades {{cluster_name}}`

- 将集群升级到新的 Kubernetes 版本：

`doctl kubernetes cluster upgrade {{cluster_name}}`

- 删除集群：

`doctl kubernetes cluster delete {{cluster_name}}`