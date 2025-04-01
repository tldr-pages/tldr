# nxc smb

> 渗透测试和利用 SMB 服务器。
> 更多信息：<https://www.netexec.wiki/smb-protocol>.

- 通过尝试指定的用户名和密码列表中的每种组合来搜索有效的域凭据：

`nxc smb {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 搜索本地账户的有效凭据，而不是域账户：

`nxc smb {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --local-auth`

- 枚举目标主机上的 SMB 共享及其指定用户的访问权限：

`nxc smb {{192.168.178.0/24}} -u {{username}} -p {{password}} --shares`

- 枚举目标主机上的网络接口，通过传递哈希值进行身份验证：

`nxc smb {{192.168.178.30-45}} -u {{username}} -H {{NTLM_hash}} --interfaces`

- 扫描目标主机以查找常见的漏洞：

`nxc smb {{path/to/target_list.txt}} -u '' -p '' -M zerologon -M petitpotam`

- 尝试在目标主机上执行命令：

`nxc smb {{192.168.178.2}} -u {{username}} -p {{password}} -x {{command}}`
