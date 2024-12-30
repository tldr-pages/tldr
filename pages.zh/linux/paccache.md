# paccache

> 一个 `pacman` 缓存清理工具。
> 更多信息：<https://manned.org/paccache>。

- 从 `pacman` 缓存中删除除最近三个软件包版本之外的所有版本：

`paccache -r`

- 设置要保留的软件包版本数量：

`paccache -rk {{num_versions}}`

- 执行干运行并显示候选删除软件包的数量：

`paccache -d`

- 将候选软件包移动到一个目录，而不是删除它们：

`paccache -m {{path/to/directory}}`