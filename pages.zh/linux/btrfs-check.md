# btrfs check

> 检查或修复 btrfs 文件系统。
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-check.html>。

- 检查 btrfs 文件系统：

`sudo btrfs check {{path/to/partition}}`

- 检查并修复 btrfs 文件系统（危险操作）：

`sudo btrfs check --repair {{path/to/partition}}`

- 显示检查的进度：

`sudo btrfs check --progress {{path/to/partition}}`

- 验证每个数据块的校验和（如果文件系统正常）：

`sudo btrfs check --check-data-csum {{path/to/partition}}`

- 使用第 `n` 个超级块（`n` 可以是 0、1 或 2）：

`sudo btrfs check --super {{n}} {{path/to/partition}}`

- 重建校验和树：

`sudo btrfs check --repair --init-csum-tree {{path/to/partition}}`

- 重建范围树：

`sudo btrfs check --repair --init-extent-tree {{path/to/partition}}`