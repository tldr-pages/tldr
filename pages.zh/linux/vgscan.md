# vgscan

> 在所有支持的逻辑卷管理器（LVM）块设备上扫描卷组。
> 另见：`lvm` 和 `vgchange`。
> 更多信息：<https://manned.org/vgscan>。

- 扫描卷组并打印找到的每个组的信息：

`sudo vgscan`

- 扫描卷组并在 `/dev` 中添加特殊文件，如果这些文件尚不存在，以便访问找到的组中的逻辑卷：

`sudo vgscan --mknodes`