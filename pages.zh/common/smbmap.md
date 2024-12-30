# smbmap

> 允许用户在整个域中枚举 Samba 共享驱动器。
> 更多信息：<https://github.com/ShawnDEvans/smbmap>。

- 枚举启用 NULL 会话和开放共享的主机：

`smbmap --host-file {{path/to/file}}`

- 枚举主机并检查 SMB 文件权限：

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q`

- 通过用户名和密码连接到 IP 或主机名：

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- 定位并下载文件 [R]ecursively 递归到 N 层深度，搜索文件名模式（正则表达式），并排除某些共享：

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q -R --depth {{number}} --exclude {{sharename}} -A {{filepattern}}`

- 通过 SMB 使用用户名和密码上传文件：

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/share_name/remote_filename}}'`