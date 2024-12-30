# linode-cli 节点负载均衡器

> 管理 Linode 节点负载均衡器。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>。

- 列出所有节点负载均衡器：

`linode-cli nodebalancers list`

- 创建一个新的节点负载均衡器：

`linode-cli nodebalancers create --region {{region}}`

- 查看特定节点负载均衡器的详细信息：

`linode-cli nodebalancers view {{nodebalancer_id}}`

- 更新现有的节点负载均衡器：

`linode-cli nodebalancers update {{nodebalancer_id}} --label {{new_label}}`

- 删除一个节点负载均衡器：

`linode-cli nodebalancers delete {{nodebalancer_id}}`

- 列出一个节点负载均衡器的配置：

`linode-cli nodebalancers configs list {{nodebalancer_id}}`

- 向节点负载均衡器添加一个新配置：

`linode-cli nodebalancers configs create {{nodebalancer_id}} --port {{port}} --protocol {{protocol}}`