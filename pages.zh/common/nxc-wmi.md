# nxc wmi

> 对 Windows Management Instrumentation (WMI) 进行渗透测试和利用。
> 更多信息：<https://www.netexec.wiki/wmi-protocol>.

- 通过尝试指定的用户名和密码列表中的每个组合来查找有效的凭据：

`nxc wmi {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 通过本地身份验证进行身份验证（而不是对域进行身份验证）：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --local-auth`

- 执行指定的 WMI 查询：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --wmi {{wmi_query}}`

- 在目标主机上执行指定的命令：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --x {{command}}`
