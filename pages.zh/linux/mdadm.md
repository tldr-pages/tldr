# mdadm

> RAID 管理工具。
> 更多信息：<https://manned.org/mdadm>。

- 创建 RAID 阵列：

`sudo mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- 停止 RAID 阵列：

`sudo mdadm --stop {{/dev/md0}}`

- 标记磁盘为故障：

`sudo mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- 从 RAID 阵列中移除磁盘：

`sudo mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- 将磁盘添加到 RAID 阵列：

`sudo mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- 显示 RAID 信息：

`sudo mdadm --detail {{/dev/md0}}`

- 通过删除 RAID 元数据来重置磁盘：

`sudo mdadm --zero-superblock {{/dev/sdXN}}`