# nxc ldap

> 通过 LDAP 渗透测试和利用 Windows Active Directory 域。
> 更多信息：<https://www.netexec.wiki/ldap-protocol>。

- 通过尝试指定列表中的每种组合的 [u] 用户名和 [p] 密码来搜索有效的域凭据：

`nxc ldap {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 枚举活动域用户：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --active-users`

- 收集有关目标域的数据并自动将这些数据导入 BloodHound：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --bloodhound --collection {{All}}`

- 尝试收集指定用户的 AS_REP 消息以执行 ASREPRoasting 攻击：

`nxc ldap {{192.168.178.2}} -u {{username}} -p '' --asreproast {{path/to/output.txt}}`

- 尝试提取域上组管理服务账户的密码：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --gmsa`