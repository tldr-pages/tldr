# devfsadm

> 用于管理 `/dev` 的管理命令。维护 `/dev` 命名空间。
> 更多信息：<https://www.unix.com/man-page/sunos/1m/devfsadm>.

- 扫描新的磁盘：

`devfsadm -c disk`

- 清理任何无效的 /dev 链接并扫描新的设备：

`devfsadm -C -v`

- 预演模式 - 输出将要进行的更改但不实际执行：

`devfsadm -C -v -n`
