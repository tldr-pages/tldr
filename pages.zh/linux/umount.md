# umount

> 从挂载点卸载文件系统，使其不再可访问。
> 当文件系统忙时，无法卸载。
> 更多信息：<https://manned.org/umount.8>.

- 通过传递挂载源的路径来卸载文件系统：

`umount {{path/to/device_file}}`

- 通过传递挂载目标的路径来卸载文件系统：

`umount {{path/to/mounted_directory}}`

- 当卸载失败时，尝试以只读方式重新挂载文件系统：

`umount {{[-r|--read-only]}} {{path/to/mounted_directory}}`

- 递归地卸载每个指定的目录：

`umount {{[-R|--recursive]}} {{path/to/mounted_directory}}`

- 卸载所有挂载的文件系统（除了 `proc` 文件系统）：

`umount {{[-a|--all]}}`