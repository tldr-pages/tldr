# uwfmgr

> 统一写过滤器 (UWF)。
> 通过将任何写入重定向到虚拟覆盖来保护驱动器。除非默认情况下已提交，否则重启后将丢弃写入。
> 更多信息：<https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>。

- 获取当前状态：

`uwfmgr get-config`

- 将驱动器设置为受保护状态：

`uwfmgr volume protect {{drive_letter}}:`

- 从保护列表中移除驱动器：

`uwfmgr volume unprotect {{drive_letter}}:`

- 启用或禁用保护（重启后生效）：

`uwfmgr filter {{enable|disable}}`

- 提交受保护驱动器上文件的更改：

`uwfmgr file commit {{drive_letter:\path\to\file}}`

- 提交受保护驱动器上文件的删除：

`uwfmgr file commit-delete {{drive_letter:\path\to\file}}`