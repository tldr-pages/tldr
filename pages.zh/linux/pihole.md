# pihole

> Pi-hole 广告拦截 DNS 服务器的终端接口。
> 更多信息：<https://docs.pi-hole.net/core/pihole-command/>.

- 检查 Pi-hole 守护进程的状态：

`pihole status`

- 更新 Pi-hole 和 Gravity：

`pihole -up`

- 监控详细系统状态：

`pihole chronometer`

- 启动或停止守护进程：

`pihole {{enable|disable}}`

- 重启守护进程（而不是服务器本身）：

`pihole restartdns`

- 将域名添加到白名单或黑名单：

`pihole {{whitelist|blacklist}} {{example.com}}`

- 在列表中搜索域名：

`pihole query {{example.com}}`

- 打开连接的实时日志：

`pihole tail`