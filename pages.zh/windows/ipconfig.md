# ipconfig

> 显示和管理 Windows 的网络配置。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 显示网络适配器列表：

`ipconfig`

- 显示网络适配器的详细列表：

`ipconfig /all`

- 为一个网络适配器重新获取 IP 地址：

`ipconfig /renew {{适配器}}`

- 为一个网络适配器释放 IP 地址：

`ipconfig /release {{适配器}}`

- 清除所有 DNS 缓存：

`ipconfig /flushdns`
