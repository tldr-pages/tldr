# fusermount

> 挂载和卸载 FUSE 文件系统。
> 更多信息：<https://manned.org/fusermount>.

- 卸载 FUSE 文件系统：

`fusermount -u {{path/to/mount_point}}`

- 当 FUSE 文件系统不再被使用时立即卸载：

`fusermount -z {{path/to/mount_point}}`

- 显示版本：

`fusermount --version`
