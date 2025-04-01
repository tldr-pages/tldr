# parted

> 分区操作程序。
> 另见：`parted-interactive`，`partprobe`。
> 更多信息：<https://www.gnu.org/software/parted/manual/html_node/Invoking-Parted.html>。

- 列出所有块设备上的分区：

`sudo parted {{[-l|--list]}}`

- 创建指定标签类型的新的分区表：

`sudo parted {{/dev/sdX}} {{[-s|--script]}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- 创建一个新的 `gpt` 分区表，其中包含一个 500MiB 的启动分区，并将剩余空间分配给系统分区：

`sudo parted {{/dev/sdX}} {{[-s|--script]}} mklabel gpt mkpart primary 0% 500MiB mkpart primary 500MiB 100%`

- 以指定磁盘启动交互模式：

`sudo parted {{/dev/sdX}}`

- 显示帮助：

`parted {{[-h|--help]}}`