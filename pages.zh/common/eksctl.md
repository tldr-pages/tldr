# eksctl

> Amazon EKS 的官方命令行工具。
> 更多信息：<https://eksctl.io>.

- 创建一个基本的集群：

`eksctl create cluster`

- 列出一个集群或所有集群的详细信息：

`eksctl get cluster --name={{name}} --region={{region}}`

- 通过配置文件创建集群：

`eksctl create cluster --config-file={{path/to/file}}`

- 使用配置文件创建集群，但跳过创建节点组，留待后续操作：

`eksctl create cluster --config-file=<path> --without-nodegroup`

- 删除一个集群：

`eksctl delete cluster --name={{name}} --region={{region}}`

- 创建集群并将集群凭据写入默认位置以外的文件：

`eksctl create cluster --name={{name}} --nodes={{4}} --kubeconfig={{path/to/config.yaml}}`

- 创建集群并阻止将集群凭据存储在本地：

`eksctl create cluster --name={{name}} --nodes={{4}} --write-kubeconfig=false`

- 创建集群并让 `eksctl` 管理 `~/.kube/eksctl/clusters` 目录下的集群凭据：

`eksctl create cluster --name={{name}} --nodes={{4}} --auto-kubeconfig`
