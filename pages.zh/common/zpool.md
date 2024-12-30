# zpool

> 管理 ZFS 池。
> 更多信息：<https://manned.org/zpool>。

- 显示所有 ZFS 池的配置和状态：

`zpool status`

- 检查 ZFS 池的错误（验证每个块的校验和）。非常消耗 CPU 和磁盘资源：

`zpool scrub {{pool_name}}`

- 列出可导入的 Zpool：

`zpool import`

- 导入一个 Zpool：

`zpool import {{pool_name}}`

- 导出一个 Zpool（卸载所有文件系统）：

`zpool export {{pool_name}}`

- 显示所有池操作的历史记录：

`zpool history {{pool_name}}`

- 创建一个镜像池：

`zpool create {{pool_name}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}`

- 向 Zpool 添加一个缓存（L2ARC）设备：

`zpool add {{pool_name}} cache {{cache_disk}}`