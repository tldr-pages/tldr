# kops

> 创建、销毁、升级和维护 Kubernetes 集群。
> 更多信息：<https://github.com/kubernetes/kops/>.

- 从配置规范创建集群：

`kops create cluster -f {{cluster_name.yaml}}`

- 创建新的 SSH 公钥：

`kops create secret sshpublickey {{key_name}} -i {{~/.ssh/id_rsa.pub}}`

- 将集群配置导出到 `~/.kube/config` 文件：

`kops export kubecfg {{cluster_name}}`

- 获取集群配置为 YAML 格式：

`kops get cluster {{cluster_name}} -o yaml`

- 删除集群：

`kops delete cluster {{cluster_name}} --yes`

- 验证集群：

`kops validate cluster {{cluster_name}} --wait {{wait_time_until_ready}} --count {{num_required_validations}}`