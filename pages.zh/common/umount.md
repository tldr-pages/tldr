# umount

> 从其挂载点解除文件系统链接，使其不再可访问。
> 当文件系统忙碌时，无法卸载。
> 更多信息：<https://man.openbsd.org/umount>。

- 通过传递挂载源的路径来卸载文件系统：

`umount {{path/to/device_file}}`

- 通过传递挂载目标的路径来卸载文件系统：

`umount {{path/to/mounted_directory}}`

- 卸载所有已挂载的文件系统（除了 `proc` 文件系统）：

`umount -a`