# zdb

> ZFS 调试器。
> 更多信息：<https://manned.org/zdb>。

- 显示所有挂载的 ZFS zpools 的详细配置：

`zdb`

- 显示特定 ZFS 池的详细配置：

`zdb -C {{poolname}}`

- 显示有关块的数量、大小和去重的统计信息：

`zdb -b {{poolname}}`