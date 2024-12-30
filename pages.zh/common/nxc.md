# nxc

> 网络服务枚举和利用工具。
> 一些子命令如 `smb` 具有自己的使用文档。
> 更多信息：<https://www.netexec.wiki/>。

- 列出指定协议的可用模块：

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -L`

- 列出指定模块的可用选项：

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -M {{module_name}} --options`

- 为模块指定一个选项：

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -M {{module_name}} -o {{OPTION_NAME}}={{option_value}}`

- 查看指定协议的可用选项：

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} --help`