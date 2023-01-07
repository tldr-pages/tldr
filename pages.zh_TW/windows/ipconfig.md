# ipconfig

> 顯示和管理 Windows 的網路設定值。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 顯示網路介面卡列表：

`ipconfig`

- 顯示網路介面卡的詳細列表：

`ipconfig /all`

- 為一個網路介面卡重新獲取 IP 地址：

`ipconfig /renew {{介面卡}}`

- 為一個網路介面卡釋放 IP 地址：

`ipconfig /release {{介面卡}}`

- 清除所有 DNS 快取：

`ipconfig /flushdns`
