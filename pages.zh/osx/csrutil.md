# csrutil

> 管理系统完整性保护配置。
> 更多信息：<https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- 显示系统完整性保护状态：

`csrutil status`

- 禁用系统完整性保护：

`csrutil disable`

- 启用系统完整性保护：

`csrutil enable`

- 显示允许的 NetBoot 源列表：

`csrutil netboot list`

- 将 IPv4 地址添加到允许的 NetBoot 源列表中：

`csrutil netboot add {{ip}}`

- 重置系统完整性保护状态并清空 NetBoot 列表：

`csrutil clear`
