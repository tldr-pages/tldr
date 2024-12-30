# nxc wmi

> 渗透测试并利用Windows管理工具（WMI）。
> 更多信息：<https://www.netexec.wiki/wmi-protocol>。

- 通过尝试指定列表中每个组合的[用]户名和[密]码来搜索有效凭据：

`nxc wmi {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 通过本地身份验证进行认证（与域认证相对）：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --local-auth`

- 发出指定的WMI查询：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --wmi {{wmi_query}}`

- 在目标主机上执行指定的命令：

`nxc wmi {{192.168.178.2}} -u {{username}} -p {{password}} --x {{command}}`