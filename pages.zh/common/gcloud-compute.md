# gcloud compute

> 在 Google Cloud 基础设施上创建、运行和管理虚拟机。
> 参见: `gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/compute>。

- 列出 Compute Engine 区域：

`gcloud compute zones list`

- 创建一个 VM 实例：

`gcloud compute instances create {{instance_name}}`

- 显示 VM 实例的详细信息：

`gcloud compute instances describe {{instance_name}}`

- 列出项目中的所有 VM 实例：

`gcloud compute instances list`

- 创建持久磁盘的快照：

`gcloud compute disks snapshot {{disk_name}} --snapshot-names {{snapshot_name}}`

- 显示快照的详细信息：

`gcloud compute snapshots describe {{snapshot_name}}`

- 删除快照：

`gcloud compute snapshots delete {{snapshot_name}}`

- 使用 SSH 连接到 VM 实例：

`gcloud compute ssh {{instance_name}}`
