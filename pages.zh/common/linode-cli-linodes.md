# linode-cli linodes

> 管理 Linode 实例。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>。

- 列出所有 Linodes：

`linode-cli linodes list`

- 创建一个新的 Linode：

`linode-cli linodes create --type {{linode_type}} --region {{region}} --image {{image_id}}`

- 查看特定 Linode 的详细信息：

`linode-cli linodes view {{linode_id}}`

- 更新 Linode 的设置：

`linode-cli linodes update {{linode_id}} --label {{[new_label}}`

- 删除一个 Linode：

`linode-cli linodes delete {{linode_id}}`

- 对 Linode 执行电源管理操作：

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- 列出可用的 Linode 备份：

`linode-cli linodes backups-list {{linode_id}}`

- 将备份恢复到 Linode：

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{backup_id}}`