# uwfmgr

> 统一写入过滤器（UWF）。
> 通过将对驱动器的所有写入操作重定向到虚拟覆盖层来保护驱动器。重启时，除非提交，否则写入的数据会被丢弃。
> 更多信息：<https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>.

- 获取当前状态：

`uwfmgr get-config`

- 设置驱动器为受保护状态：

`uwfmgr volume protect {{drive_letter}}:`

- 从保护列表中移除驱动器：

`uwfmgr volume unprotect {{drive_letter}}:`

- 启用或禁用保护（重启后生效）：

`uwfmgr filter {{enable|disable}}`

- 提交保护驱动器上文件的更改：

`uwfmgr file commit {{drive_letter:\path\to\file}}`

- 提交删除保护驱动器上的文件：

`uwfmgr file commit-delete {{drive_letter:\path\to\file}}`