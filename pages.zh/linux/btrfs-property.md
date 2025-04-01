# btrfs property

> 获取、设置或列出 BTRFS 文件系统对象（文件、目录、子卷、文件系统或设备）的属性。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-property.html>。

- 列出给定 BTRFS 对象的可用属性（及描述）：

`sudo btrfs property list {{path/to/btrfs_object}}`

- 获取给定 BTRFS 对象的所有属性：

`sudo btrfs property get {{path/to/btrfs_object}}`

- 获取给定 BTRFS 文件系统或设备的 `label` 属性：

`sudo btrfs property get {{path/to/btrfs_filesystem}} label`

- 获取给定 BTRFS 文件系统或设备的所有特定对象类型的属性：

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{path/to/btrfs_filesystem}}`

- 设置给定 BTRFS inode（文件或目录）的 `compression` 属性：

`sudo btrfs property set {{path/to/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`