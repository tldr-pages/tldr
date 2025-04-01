# pihole

> 管理 Pi-hole 广告拦截 DNS 服务器。
> 更多信息：<https://docs.pi-hole.net/main/pihole-command>.

- 检查 Pi-hole 守护进程的状态：

`pihole status`

- 更新 Pi-hole 和 Gravity：

`pihole {{[-up|updatePihole]}}`

- 启动或停止守护进程：

`pihole {{enable|disable}}`

- 更新列表并清空缓存，但不重启 DNS 服务器：

`pihole reloaddns`

- 更新广告服务器域名列表：

`pihole {{[-g|updateGravity]}}`

- 允许或拒绝指定的域名：

`pihole {{allowlist|denylist}} {{example.com}}`

- 搜索列表中的域名：

`pihole {{[-q|query]}} {{example.com}}`

- 打开实时连接日志：

`pihole {{[-t|tail]}}`
