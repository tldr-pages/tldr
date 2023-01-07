# getmac

> 显示系统的 MAC 地址。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- 显示当前系统的 MAC 地址：

`getmac`

- 以特定格式显示详细信息：

`getmac /fo {{table|list|csv}}`

- 排除输出列表中的标题：

`getmac /nh`

- 显示一个远程主机的 MAC 地址：

`getmac /s {{主机名}} /u {{用户名}} /p {{密码}}`

- 详细显示 MAC 地址信息：

`getmac /v`

- 显示详细的帮助信息：

`getmac /?`
