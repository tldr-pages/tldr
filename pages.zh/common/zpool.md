# zpool

> 管理 ZFS 池。
> 更多信息：<https://manned.org/zpool>.

- 显示所有 ZFS 池的配置和状态：

`zpool status`

- 检查 ZFS 池是否有错误（验证每个块的校验和）。非常消耗 CPU 和磁盘资源：

`zpool scrub {{池名称}}`

- 列出可导入的 ZFS 池：

`zpool import`

- 导入一个 ZFS 池：

`zpool import {{池名称}}`

- 导出一个 ZFS 池（卸载所有文件系统）：

`zpool export {{池名称}}`

- 显示所有池操作的历史记录：

`zpool history {{池名称}}`

- 创建一个镜像池：

`zpool create {{池名称}} mirror {{磁盘1}} {{磁盘2}} mirror {{磁盘3}} {{磁盘4}}`

- 向 ZFS 池添加一个缓存（L2ARC）设备：

`zpool add {{池名称}} cache {{缓存磁盘}}`
