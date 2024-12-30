# umount

> 从其挂载点取消链接文件系统，使其不再可访问。
> 当文件系统处于忙状态时，无法卸载。
> 更多信息：<https://manned.org/umount.8>。

- 通过传递其挂载源的路径卸载文件系统：

`umount {{path/to/device_file}}`

- 通过传递其挂载目标的路径卸载文件系统：

`umount {{path/to/mounted_directory}}`

- 当卸载失败时，尝试以只读方式重新挂载文件系统：

`umount --read-only {{path/to/mounted_directory}}`

- 递归卸载每个指定目录：

`umount --recursive {{path/to/mounted_directory}}`

- 卸载所有已挂载的文件系统（除了 `proc` 文件系统）：

`umount -a`