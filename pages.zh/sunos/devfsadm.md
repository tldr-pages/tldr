# devfsadm

> `/dev` 的管理命令。维护 `/dev` 命名空间。
> 更多信息：<https://www.unix.com/man-page/sunos/1m/devfsadm>。

- 扫描新磁盘：

`devfsadm -c disk`

- 清理任何悬挂的 /dev 链接并扫描新设备：

`devfsadm -C -v`

- 干运行 - 输出将要更改的内容，但不进行任何修改：

`devfsadm -C -v -n`