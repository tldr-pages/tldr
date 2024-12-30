# linode-cli 卷

> 管理 Linode 卷。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>。

- 列出当前的卷：

`linode-cli volumes list`

- 创建一个新卷并将其附加到特定的 Linode：

`linode-cli volumes create --label {{volume_label}} --size {{size_in_GB}} --linode-id {{linode_id}}`

- 将卷附加到特定的 Linode：

`linode-cli volumes attach {{volume_id}} --linode-id {{linode_id}}`

- 从 Linode 中分离卷：

`linode-cli volumes detach {{volume_id}}`

- 调整卷的大小（注意：大小只能增加）：

`linode-cli volumes resize {{volume_id}} --size {{new_size_in_GB}}`

- 删除卷：

`linode-cli volumes delete {{volume_id}}`