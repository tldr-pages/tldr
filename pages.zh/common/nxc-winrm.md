# nxc winrm

> 渗透测试并利用Windows远程管理（winrm）。
> 更多信息请访问：<https://www.netexec.wiki/winrm-protocol>。

- 通过尝试指定的用户名和密码列表中的每种组合来搜索有效凭据：

`nxc winrm {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 指定要进行身份验证的域（避免初始的SMB连接）：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -d {{domain_name}}`

- 在主机上执行指定的命令：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -x {{whoami}}`

- 以管理员身份使用LAPS在主机上执行指定的PowerShell命令：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} --laps -X {{whoami}}`