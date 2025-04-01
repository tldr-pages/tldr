# quotacheck

> 扫描文件系统的磁盘使用情况；创建、检查和修复配额文件。
> 最好关闭配额后再运行配额检查，以防配额文件受损或丢失。
> 更多信息：<https://manned.org/quotacheck>.

- 检查所有已挂载的非NFS文件系统的配额：

`sudo quotacheck --all`

- 即使配额已启用也强制检查（这可能会导致配额文件受损或丢失）：

`sudo quotacheck --force {{mountpoint}}`

- 以调试模式检查指定文件系统的配额：

`sudo quotacheck --debug {{mountpoint}}`

- 检查指定文件系统的配额，并显示进度：

`sudo quotacheck --verbose {{mountpoint}}`

- 检查用户配额：

`sudo quotacheck --user {{user}} {{mountpoint}}`

- 检查组配额：

`sudo quotacheck --group {{group}} {{mountpoint}}`
