# swapon

> 启用设备和文件进行交换。
> 注意：`path/to/file` 可以指向一个常规文件或交换分区。
> 更多信息：<https://manned.org/swapon>。

- 显示交换信息：

`swapon`

- 启用指定的交换区域：

`swapon {{path/to/file}}`

- 启用 `/etc/fstab` 中指定的所有交换区域，除了那些带有 `noauto` 选项的：

`swapon --all`

- 通过标签启用交换分区：

`swapon -L {{label}}`