# smbmap

> 枚举整个域中的 Samba 共享驱动器。
> 更多信息：<https://github.com/ShawnDEvans/smbmap>.

- 枚举启用 NULL 会话并开放共享的主机：

`smbmap --host-file {{path/to/file}}`

- 显示主机上的 SMB 共享和权限，提示用户输入密码或 NTLM 散列：

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}}`

- 在远程系统上执行 shell 命令：

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}} -x {{command}}`

- 枚举主机并检查 SMB 文件权限：

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q`

- 通过 SMB 使用用户名和密码连接到 IP 地址或主机名：

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- 递归定位和下载文件，搜索文件名模式（正则表达式），并排除某些共享：

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q -R --depth {{number}} --exclude {{sharename}} -A {{filepattern}}`

- 通过 SMB 使用用户名和密码上传文件：

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/share_name/remote_filename}}'`

- 显示 SMB 共享并递归列出目录和文件，搜索匹配正则表达式的内容：

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}} -R -F {{pattern}}`
