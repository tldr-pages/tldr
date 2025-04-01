# swapoff

> 禁用交换设备和文件。
> 注意：`path/to/file` 可以指向普通文件或交换分区。
> 更多信息：<https://manned.org/swapoff.8>.

- 禁用指定的交换区域：

`swapoff {{path/to/file}}`

- 禁用 `/proc/swaps` 中的所有交换区域：

`swapoff {{[-a|--all]}}`

- 通过标签禁用交换分区：

`swapoff -L {{label}}`
