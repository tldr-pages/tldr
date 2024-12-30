# linode-cli 工单

> 管理 Linode 支持工单。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>。

- 列出您的支持工单：

`linode-cli tickets list`

- 打开一个新工单：

`linode-cli tickets create --summary "{{工单的摘要或快速标题}}" --description "{{问题的详细描述}}"`

- 列出工单的回复：

`linode-cli tickets replies {{ticket_id}}`

- 回复特定工单：

`linode-cli tickets reply {{ticket_id}} --description "{{您的回复内容}}"`