# zramctl

> 设置和控制 zram 设备。
> 使用 `mkfs` 或 `mkswap` 格式化 zram 设备为分区。
> 更多信息：<https://manned.org/zramctl>。

- 检查 zram 是否已启用：

`lsmod | grep -i zram`

- 启用具有动态设备数量的 zram（使用 `zramctl` 进一步配置设备）：

`sudo modprobe zram`

- 启用具有确切 2 个设备的 zram：

`sudo modprobe zram num_devices={{2}}`

- 查找并初始化下一个空闲的 zram 设备为一个 2 GB 的虚拟驱动器，使用 LZ4 压缩：

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- 列出当前已初始化的设备：

`sudo zramctl`