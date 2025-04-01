# mkswap

> 在设备或文件上设置 Linux 交换区域。
> 注意：`path/to/file` 可以指向常规文件或交换分区。
> 更多信息：<https://manned.org/mkswap>.

- 设置指定的交换区域：

`sudo mkswap {{path/to/file}}`

- 在创建交换区域之前检查分区的坏块：

`sudo mkswap {{[-c|--check]}} {{path/to/file}}`

- 为分区指定标签（允许 `swapon` 使用该标签）：

`sudo mkswap {{[-L|--label]}} {{label}} {{/dev/sda1}}`
