# nxc mssql

> 测试和利用 Microsoft SQL 服务器。
> 更多信息：<https://www.netexec.wiki/mssql-protocol>.

- 通过尝试指定的用户名和密码列表中的所有组合来查找有效的凭据：

`nxc mssql {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- 在目标服务器上执行指定的 SQL [q]uery：

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --query '{{SELECT * FROM sys.databases;}}'`

- 通过 MSSQL 在目标服务器上执行指定的 shell 命令：

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} -x {{whoami}}`

- 通过 MSSQL 在目标服务器上执行指定的 PowerShell 命令，不获取输出：

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} -X {{whoami}} --no-output`

- 从目标服务器下载远程文件并将其存储在指定位置：

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --get-file {{C:\path\to\remote_file}} {{path/to/local_file}}`

- 将本地文件上传到目标服务器的指定位置：

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --put-file {{path/to/local_file}} {{C:\path\to\remote_file}}`
