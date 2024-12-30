# btrfs 恢复

> 尝试从损坏的 btrfs 文件系统中恢复文件。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>。

- 将所有文件从 btrfs 文件系统恢复到指定目录：

`sudo btrfs restore {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 列出（不写入）要从 btrfs 文件系统恢复的文件：

`sudo btrfs restore --dry-run {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 从 btrfs 文件系统中恢复匹配给定正则表达式（不区分大小写）的文件（目标文件的所有父目录也必须匹配）：

`sudo btrfs restore --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 使用特定的根树 `bytenr` 从 btrfs 文件系统恢复文件（参见 `btrfs-find-root`）：

`sudo btrfs restore -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 从 btrfs 文件系统恢复文件（包括元数据、扩展属性和符号链接），覆盖目标中的文件：

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{path/to/btrfs_device}} {{path/to/target_directory}}`