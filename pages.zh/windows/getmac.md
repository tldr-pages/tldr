# getmac

> 显示系统的MAC地址。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>。

- 显示当前系统的MAC地址：

`getmac`

- 以特定格式显示详细信息：

`getmac /fo {{table|list|csv}}`

- 在输出列表中排除标题：

`getmac /nh`

- 显示远程计算机的MAC地址：

`getmac /s {{hostname}} /u {{username}} /p {{password}}`

- 显示带有详细信息的MAC地址：

`getmac /v`

- 显示帮助信息：

`getmac /?`