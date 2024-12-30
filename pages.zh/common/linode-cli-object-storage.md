# linode-cli 对象存储

> 管理 Linode 对象存储。
> 另见：`linode-cli`。
> 更多信息：<https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>。

- 列出所有对象存储桶：

`linode-cli object-storage buckets list`

- 创建一个新的对象存储桶：

`linode-cli object-storage buckets create --cluster {{cluster_id}} --label {{bucket_label}}`

- 删除一个对象存储桶：

`linode-cli object-storage buckets delete {{cluster_id}} {{bucket_label}}`

- 列出对象存储集群区域：

`linode-cli object-storage clusters list`

- 列出对象存储的访问密钥：

`linode-cli object-storage keys list`

- 为对象存储创建一个新的访问密钥：

`linode-cli object-storage keys create --label {{label}}`

- 撤销对象存储的访问密钥：

`linode-cli object-storage keys revoke {{access_key_id}}`