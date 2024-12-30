# smbmap

> SMB枚举工具。
> 更多信息：<https://github.com/ShawnDEvans/smbmap>。

- 显示主机上的SMB共享和权限，提示用户输入密码或NTLM哈希：

`smbmap -u {{username}} --prompt -H {{ip}}`

- 显示主机上的SMB共享和权限，指定域并传入密码NTLM哈希：

`smbmap -u {{username}} --prompt -d {{domain}} -H {{ip}}`

- 显示SMB共享并列出单级目录和文件：

`smbmap -u {{username}} --prompt -H {{ip}} -r`

- 显示SMB共享并递归列出定义级别的目录和文件：

`smbmap -u {{username}} --prompt -H {{ip}} -R --depth {{3}}`

- 显示SMB共享并递归列出目录和文件，下载与正则表达式匹配的文件：

`smbmap -u {{username}} --prompt -H {{ip}} -R -A {{pattern}}`

- 显示SMB共享并递归列出目录和文件，搜索文件内容与正则表达式匹配：

`smbmap -u {{username}} --prompt -H {{ip}} -R -F {{pattern}}`

- 在远程系统上执行shell命令：

`smbmap -u {{username}} --prompt -H {{ip}} -x {{command}}`

- 将文件上传到远程系统：

`smbmap -u {{username}} --prompt -H {{ip}} --upload {{source}} {{destination}}`