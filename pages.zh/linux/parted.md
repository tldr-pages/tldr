# parted

> 一个分区操作程序。
> 另见：`partprobe`。
> 更多信息：<https://www.gnu.org/software/parted/parted.html>。

- 列出所有块设备上的分区：

`sudo parted --list`

- 启动交互模式并选择指定的磁盘：

`sudo parted {{/dev/sdX}}`

- 创建指定标签类型的新分区表：

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- 在交互模式下显示分区信息：

`print`

- 在交互模式下选择磁盘：

`select {{/dev/sdX}}`

- 在交互模式下创建一个16 GB的分区，并指定文件系统：

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- 在交互模式下调整分区大小：

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- 在交互模式下删除分区：

`rm {{/dev/sdXN}}`