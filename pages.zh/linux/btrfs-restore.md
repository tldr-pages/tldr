# btrfs restore

> 尝试从损坏的 btrfs 文件系统中恢复文件。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- 从 btrfs 文件系统中恢复所有文件到指定目录：

`sudo btrfs restore {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 列出（不写入）从 btrfs 文件系统中要恢复的文件：

`sudo btrfs restore --dry-run {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 恢复与给定正则表达式匹配的文件（[c]ase-insensitive），从 btrfs 文件系统中恢复文件（目标文件的所有父目录也必须匹配）：

`sudo btrfs restore --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 使用特定的根树 `bytenr`（参见 `btrfs-find-root`）从 btrfs 文件系统中恢复文件：

`sudo btrfs restore -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- 从 btrfs 文件系统中恢复文件（包括元数据、扩展属性和符号链接），覆盖目标目录中的文件：

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{path/to/btrfs_device}} {{path/to/target_directory}}`
