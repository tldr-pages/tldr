# vgscan

> 在所有支持的逻辑卷管理器（LVM）块设备上扫描卷组。
> 参见：`lvm` 和 `vgchange`。
> 更多信息：<https://manned.org/vgscan>。

- 扫描卷组并打印每个发现的卷组的信息：

`sudo vgscan`

- 扫描卷组并在 `/dev` 目录中添加访问逻辑卷所需的特殊文件（如果这些文件不存在）：

`sudo vgscan --mknodes`
