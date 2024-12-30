# eksctl

> Amazon EKS 的官方命令行工具。
> 更多信息：<https://eksctl.io>。

- 创建一个基本的集群：

`eksctl create cluster`

- 列出关于某个集群或所有集群的详细信息：

`eksctl get cluster --name={{name}} --region={{region}}`

- 创建一个集群，将所有配置信息传递到一个文件中：

`eksctl create cluster --config-file={{path/to/file}}`

- 使用配置文件创建集群，并跳过节点组的创建，稍后再创建：

`eksctl create cluster --config-file=<path> --without-nodegroup`

- 删除一个集群：

`eksctl delete cluster --name={{name}} --region={{region}}`

- 创建集群并将集群凭证写入到默认之外的文件：

`eksctl create cluster --name={{name}} --nodes={{4}} --kubeconfig={{path/to/config.yaml}}`

- 创建一个集群并防止在本地存储集群凭证：

`eksctl create cluster --name={{name}} --nodes={{4}} --write-kubeconfig=false`

- 创建一个集群并让 `eksctl` 在 `~/.kube/eksctl/clusters` 目录下管理集群凭证：

`eksctl create cluster --name={{name}} --nodes={{4}} --auto-kubeconfig`