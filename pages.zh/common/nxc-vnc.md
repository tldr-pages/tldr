# nxc vnc

> 渗透测试和利用 VNC 服务器。
> 更多信息：<https://www.netexec.wiki/>。

- 通过尝试指定的用户名和密码列表中的所有组合来查找有效的凭证：

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 通过 VNC-sleep 避免速率限制：

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --vnc-sleep {{10}}`

- 在等待指定时间后在远程系统上截取屏幕截图：

`nxc vnc {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`
