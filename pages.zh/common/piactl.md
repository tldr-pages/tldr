# piactl

> Private Internet Access 的命令行工具，一个商业 VPN 服务提供商。
> 更多信息：<https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>。

- 登录 Private Internet Access：

`piactl login {{path/to/login_file}}`

- 连接到 Private Internet Access：

`piactl connect`

- 从 Private Internet Access 断开连接：

`piactl disconnect`

- 启用或禁用后台运行的 Private Internet Access 守护进程：

`piactl background {{enable|disable}}`

- 列出所有可用的 VPN 区域：

`piactl get regions`

- 显示当前的 VPN 区域：

`piactl get region`

- 设置您的 VPN 区域：

`piactl set region {{region}}`

- 登出 Private Internet Access：

`piactl logout`