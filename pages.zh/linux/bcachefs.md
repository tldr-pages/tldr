# bcachefs

> 管理 `bcachefs` 文件系统/设备。
> 一些子命令（如 `device`）有自己的使用文档。
> 更多信息：<https://bcachefs-docs.readthedocs.io/en/latest/index.html>.

- 使用 `bcachefs` 格式化分区：

`sudo bcachefs format {{path/to/partition}}`

- 挂载 `bcachefs` 文件系统：

`sudo bcachefs mount {{path/to/partition}} {{path/to/mountpoint}}`

- 创建一个 RAID 0 文件系统，其中 SSD 用作缓存，HDD 用作长期存储：

`sudo bcachefs format --label=ssd.ssd1 {{path/to/ssd/partition}} --label=hdd.hdd1 {{path/to/hdd/partition}} --replicas=1 --foreground_target=ssd --promote_target=ssd --background_target=hdd`

- 挂载多设备文件系统：

`sudo bcachefs mount {{path/to/partition1}}:{{path/to/partition2}} {{path/to/mountpoint}}`

- 显示磁盘使用情况：

`bcachefs fs usage --human-readable {{path/to/mountpoint}}`

- 格式化和挂载后设置副本：

`sudo bcachefs set-fs-option --metadata_replicas={{2}} --data_replicas={{2}} {{path/to/partition}}`

- 强制 `bcachefs` 确保所有文件都被复制：

`sudo bcachefs data rereplicate {{path/to/mountpoint}}`

- 显示帮助：

`bcachefs`