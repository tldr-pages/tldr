# paccache

> 一个 `pacman` 缓存清理工具。
> 更多信息：<https://manned.org/paccache>.

- 从 `pacman` 缓存中删除除最新 3 个版本之外的所有软件包版本：

`paccache -r`

- 设置保留的软件包版本数量：

`paccache -rk {{num_versions}}`

- 执行模拟运行并显示待删除的软件包数量：

`paccache -d`

- 将待删除的软件包移动到指定目录而不是直接删除：

`paccache -m {{path/to/directory}}`
