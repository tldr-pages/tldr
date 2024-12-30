# swapoff

> 禁用设备和文件的交换。
> 注意：`path/to/file` 可以指向常规文件或交换分区。
> 更多信息：<https://manned.org/swapoff>。

- 禁用指定的交换区：

`swapoff {{path/to/file}}`

- 禁用 `/proc/swaps` 中的所有交换区：

`swapoff --all`

- 通过标签禁用交换分区：

`swapoff -L {{label}}`