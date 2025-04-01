# linode-cli nodebalancers

> 管理 Linode NodeBalancers。
> 参见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>。

- 列出所有 NodeBalancers：

`linode-cli nodebalancers list`

- 创建新的 NodeBalancer：

`linode-cli nodebalancers create --region {{region}}`

- 查看特定 NodeBalancer 的详情：

`linode-cli nodebalancers view {{nodebalancer_id}}`

- 更新现有的 NodeBalancer：

`linode-cli nodebalancers update {{nodebalancer_id}} --label {{new_label}}`

- 删除 NodeBalancer：

`linode-cli nodebalancers delete {{nodebalancer_id}}`

- 列出 NodeBalancer 的配置：

`linode-cli nodebalancers configs list {{nodebalancer_id}}`

- 为 NodeBalancer 添加新的配置：

`linode-cli nodebalancers configs create {{nodebalancer_id}} --port {{port}} --protocol {{protocol}}`
