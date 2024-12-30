# systemd-repart

> 自动扩展和添加分区。
> 根据repart.d中描述的配置文件扩展和添加分区。
> 不会自动调整分区上的文件系统大小。请参阅systemd-growfs以扩展文件系统。
> 更多信息请访问：<https://www.freedesktop.org/software/systemd/man/systemd-repart.html>。

- 将根分区（/）扩展到所有可用磁盘空间：

`systemd-repart`

- 查看更改但不应用：

`systemd-repart --dry-run=yes`

- 将根分区大小扩展到10千兆字节：

`systemd-repart --size=10G --root /`