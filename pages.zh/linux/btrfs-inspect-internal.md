# btrfs inspect-internal

> 查询 Btrfs 文件系统的内部信息。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- 打印超级块的信息：

`sudo btrfs inspect-internal dump-super {{path/to/partition}}`

- 打印超级块及其所有副本的信息：

`sudo btrfs inspect-internal dump-super --all {{path/to/partition}}`

- 打印文件系统的元数据信息：

`sudo btrfs inspect-internal dump-tree {{path/to/partition}}`

- 打印第 `n` 个 i-node 中的文件列表：

`sudo btrfs inspect-internal inode-resolve {{n}} {{path/to/btrfs_mount}}`

- 打印给定逻辑地址处的文件列表：

`sudo btrfs inspect-internal logical-resolve {{logical_address}} {{path/to/btrfs_mount}}`

- 打印根树、扩展树、校验和树和文件系统树的统计信息：

`sudo btrfs inspect-internal tree-stats {{path/to/partition}}`