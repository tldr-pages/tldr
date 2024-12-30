# mkfs.btrfs

> 创建一个 BTRFS 文件系统。
> 默认使用 `raid1`，这意味着在两个不同设备上存储数据块的两个副本。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>。

- 在单个设备上创建 btrfs 文件系统：

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- 在多个设备上创建带有 raid1 的 btrfs 文件系统：

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- 为文件系统设置标签：

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`