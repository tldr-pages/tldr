# findmnt

> 查找文件系统。
> 更多信息：<https://manned.org/findmnt>。

- 列出所有已挂载的文件系统：

`findmnt`

- 搜索设备：

`findmnt {{/dev/sdb1}}`

- 搜索挂载点：

`findmnt {{/}}`

- 查找特定类型的文件系统：

`findmnt {{[-t|--types]}} {{ext4}}`

- 查找带有特定标签的文件系统：

`findmnt LABEL={{BigStorage}}`

- 详细检查挂载表内容并验证 `/etc/fstab`：

`findmnt {{[-x|--verify]}} --verbose`