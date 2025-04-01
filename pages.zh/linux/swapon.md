# swapon

> 启用设备和文件作为交换空间。
> 注意：`path/to/file` 可以指向一个普通文件或一个交换分区。
> 更多信息：<https://manned.org/swapon.8>.

- 显示交换空间信息：

`swapon`

- 启用指定的交换区域：

`swapon {{path/to/file}}`

- 启用 `/etc/fstab` 中指定的所有交换区域，但不包括带有 `noauto` 选项的那些：

`swapon {{[-a|--all]}}`

- 通过标签启用交换分区：

`swapon -L {{label}}`
