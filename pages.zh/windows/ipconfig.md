# ipconfig

> 显示和管理 Windows 的网络配置。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>。

- 列出所有网络适配器：

`ipconfig`

- 显示网络适配器的详细列表：

`ipconfig /all`

- 续租网络适配器的 IP 地址：

`ipconfig /renew {{adapter}}`

- 释放网络适配器的 IP 地址：

`ipconfig /release {{adapter}}`

- 显示本地 DNS 缓存：

`ipconfig /displaydns`

- 从本地 DNS 缓存中移除所有数据：

`ipconfig /flushdns`