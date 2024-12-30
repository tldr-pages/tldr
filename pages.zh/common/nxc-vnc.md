# nxc vnc

> 渗透测试和利用 VNC 服务器。
> 更多信息：<https://www.netexec.wiki/>.

- 通过尝试指定的 [u] 用户名和 [p] 密码列表中的每种组合来寻找有效凭据：

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 通过 VNC-sleep 避免速率限制：

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --vnc-sleep {{10}}`

- 在等待指定时间后对远程系统进行截图：

`nxc vnc {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`