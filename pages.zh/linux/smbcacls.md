# smbcacls

> 查看和操作 SMB 共享上的 Windows 访问控制列表 (ACL)。
> Samba 套件的一部分。
> 更多信息：<https://www.samba.org/samba/docs/current/man-html/smbcacls.1.html>.

- 显示远程 SMB 共享上的文件或目录的 ACL：

`smbcacls //{{server}}/{{share}} {{path/to/file_or_directory}} --user {{domain\\username}}%{{password}}`

- 为远程 SMB 共享上的文件设置新的 ACL（将 `"ACL:..."` 替换为有效的 Windows ACL 规范）：

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{domain\\username}}%{{password}} "ACL:{{DACL}}"`

- 删除所有现有的 ACL 条目并设置新的 ACL：

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{domain\\username}}%{{password}} "RESET" "ACL:{{DACL}}"`

- 指定一个替代的工作组（或域），并让程序交互式地提示输入密码：

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{username}} --workgroup {{workgroup}}`