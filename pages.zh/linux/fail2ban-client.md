# fail2ban-client

> 配置和控制 fail2ban 服务器。
> 更多信息：<https://github.com/fail2ban/fail2ban>。

- 获取监狱服务的当前状态：

`fail2ban-client status {{jail}}`

- 从监狱服务的禁用列表中移除指定的 IP：

`fail2ban-client set {{jail}} unbanip {{ip}}`

- 验证 fail2ban 服务器是否正常运行：

`fail2ban-client ping`