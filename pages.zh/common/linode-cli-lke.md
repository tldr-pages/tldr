# linode-cli lke

> 管理 Linode Kubernetes Engine (LKE) 集群。
> 参见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-lke>。

- 列出所有 LKE 集群：

`linode-cli lke clusters list`

- 创建新的 LKE 集群：

`linode-cli lke clusters create --region {{region}} --type {{type}} --node-type {{node_type}} --nodes-count {{count}}`

- 查看特定 LKE 集群的详细信息：

`linode-cli lke clusters view {{cluster_id}}`

- 更新现有 LKE 集群：

`linode-cli lke clusters update {{cluster_id}} --node-type {{new_node_type}}`

- 删除 LKE 集群：

`linode-cli lke clusters delete {{cluster_id}}`
