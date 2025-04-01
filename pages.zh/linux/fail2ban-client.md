# fail2ban-client

> 配置和控制 fail2ban 服务器。
> 更多信息：<https://github.com/fail2ban/fail2ban>.

- 获取指定 jails 服务的当前状态：

`fail2ban-client status {{jail}}`

- 从指定 jails 服务的封禁列表中移除指定的 IP：

`fail2ban-client set {{jail}} unbanip {{ip}}`

- 检查 fail2ban 服务器是否在线：

`fail2ban-client ping`
