# kubeadm

> 用于创建和管理 Kubernetes 集群的命令行接口。
> 更多信息：<https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- 创建 Kubernetes 控制平面：

`kubeadm init`

- 引导 Kubernetes 工作节点并将其加入集群：

`kubeadm join --token {{token}}`

- 创建一个有效期为 12 小时的新引导令牌：

`kubeadm token create --ttl {{12h0m0s}}`

- 检查 Kubernetes 集群是否可升级，并查看可用的版本：

`kubeadm upgrade plan`

- 将 Kubernetes 集群升级到指定版本：

`kubeadm upgrade apply {{version}}`

- 查看包含集群配置的 kubeadm ConfigMap：

`kubeadm config view`

- 撤销 'kubeadm init' 或 'kubeadm join' 对主机所做的更改：

`kubeadm reset`
