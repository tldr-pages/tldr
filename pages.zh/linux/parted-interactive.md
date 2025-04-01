# parted

> 一个分区操作程序。
> 另见: `parted`, `partprobe`。
> 更多信息: <https://www.gnu.org/software/parted/parted.html>。

- 以指定磁盘启动交互模式：

`sudo parted {{/dev/sdX}}`

- 在交互模式下显示分区信息：

`print`

- 在交互模式下选择一个磁盘：

`select {{/dev/sdX}}`

- 在交互模式下创建一个16GB的分区并指定文件系统类型：

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- 在交互模式下调整分区大小：

`resizepart {{/dev/sdXN}} {{分区结束位置}}`

- 在交互模式下删除一个分区：

`rm {{/dev/sdXN}}`

- 显示帮助：

`?`
