# piactl

> 这是一个用于私人互联网访问（Private Internet Access）的命令行工具，私人互联网访问是一家商业VPN提供商。
> 更多信息：<https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>。

- 登录私人互联网访问：

`piactl login {{path/to/login_file}}`

- 连接到私人互联网访问：

`piactl connect`

- 断开与私人互联网访问的连接：

`piactl disconnect`

- 在后台启用或禁用私人互联网访问守护进程：

`piactl background {{enable|disable}}`

- 列出所有可用的VPN区域：

`piactl get regions`

- 显示当前的VPN区域：

`piactl get region`

- 设置你的VPN区域：

`piactl set region {{region}}`

- 从私人互联网访问登出：

`piactl logout`