# nxc winrm

> 对 Windows 远程管理 (winrm) 进行渗透测试和攻击。
> 更多信息：<https://www.netexec.wiki/winrm-protocol>。

- 通过尝试指定的用户名和密码列表中的每种组合来查找有效的凭据：

`nxc winrm {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 指定要验证的域（避免初始 SMB 连接）：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -d {{domain_name}}`

- 在主机上执行指定的命令：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -x {{whoami}}`

- 使用 LAPS 以管理员身份在主机上执行指定的 PowerShell 命令：

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} --laps -X {{whoami}}`