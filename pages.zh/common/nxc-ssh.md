# nxc ssh

> 渗透测试和利用 SSH 服务器。
> 参见：`hydra`。
> 更多信息：<https://www.netexec.wiki/ssh-protocol>.

- 对指定目标上的用户名列表使用指定的 [p]assword 进行喷洒攻击：

`nxc ssh {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{password}}`

- 通过尝试指定的用户名列表和密码列表中的每一种组合来查找有效的凭据：

`nxc ssh {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 使用指定的私钥进行身份验证，并使用提供的 [p]assword 作为密钥的密码：

`nxc ssh {{192.186.178.2}} -u {{path/to/usernames.txt}} -p {{password}} --key-file {{path/to/id_rsa}}`

- 在多个目标上尝试 [u]sername 和 [p]assword 的组合：

`nxc ssh {{192.168.178.0/24}} -u {{username}} -p {{password}}`

- 成功登录后检查 `sudo` 权限：

`nxc ssh {{192.168.178.2}} -u {{username}} -p {{path/to/passwords.txt}} --sudo-check`