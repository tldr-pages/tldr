# nxc rdp

> 渗透测试和利用 RDP 服务器。
> 更多信息：<https://www.netexec.wiki/rdp-protocol>。

- 通过尝试指定的 [u] 用户名和 [p] 密码列表中的每种组合来搜索有效凭据：

`nxc rdp {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 等待指定的秒数后截图：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`

- 在指定的分辨率下截图：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --res {{1024x768}}`

- 如果网络级身份验证被禁用，截图 RDP 登录提示：

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --nla-screenshot`