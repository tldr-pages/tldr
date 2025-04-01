# linode-cli tickets

> 管理 Linode 支持工单。
> 参见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>。

- 列出您的支持工单：

`linode-cli tickets list`

- 创建新的工单：

`linode-cli tickets create --summary "{{工单的简要标题或总结}}" --description "{{问题的详细描述}}"`

- 列出某个工单的回复：

`linode-cli tickets replies {{ticket_id}}`

- 回复某个特定的工单：

`linode-cli tickets reply {{ticket_id}} --description "{{您的回复内容}}"`