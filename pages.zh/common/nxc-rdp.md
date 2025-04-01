# nxc rdp

> 渗透测试和利用 RDP 服务器。
> 更多信息：<https://www.netexec.wiki/rdp-protocol>.

- 通过尝试指定的用户名和密码列表中的每种组合来查找有效的凭证：

`nxc rdp {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 在等待指定的秒数后截取屏幕截图：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`

- 在指定的分辨率下截取屏幕截图：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --res {{1024x768}}`

- 如果禁用了网络级身份验证，截取 RDP 登录提示的屏幕截图：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --nla-screenshot`