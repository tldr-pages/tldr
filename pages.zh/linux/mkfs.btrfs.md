# mkfs.btrfs

> 创建一个 BTRFS 文件系统。
> 默认情况下是 `raid1`，指定了数据块的两份拷贝分布在两个不同的设备上。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- 在单个设备上创建一个 btrfs 文件系统：

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- 在多个设备上使用 raid1 创建一个 btrfs 文件系统：

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- 为文件系统设置一个标签（可选）：

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`
