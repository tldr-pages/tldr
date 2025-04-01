# zramctl

> 设置和控制 zram 设备。
> 使用 `mkfs` 或 `mkswap` 将 zram 设备格式化为分区。
> 更多信息：<https://manned.org/zramctl>。

- 检查 zram 是否已启用：

`lsmod | grep {{[-i|--ignore-case]}} zram`

- 以动态数量的设备启用 zram（使用 `zramctl` 进一步配置设备）：

`sudo modprobe zram`

- 启用 zram 并指定恰好 2 个设备：

`sudo modprobe zram num_devices={{2}}`

- 查找并初始化下一个空闲的 zram 设备为 2 GB 的虚拟磁盘，使用 LZ4 压缩：

`sudo zramctl {{[-f|--find]}} {{[-s|--size]}} {{2GB}} {{[-a|--algorithm]}} {{lz4}}`

- 列出当前已初始化的设备：

`sudo zramctl`