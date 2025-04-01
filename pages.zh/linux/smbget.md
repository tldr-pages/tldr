# smbget

> 类似 `wget` 的工具，用于从 SMB 服务器下载文件。
> 更多信息：<https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- 从服务器下载文件：

`smbget {{smb://server/share/file}}`

- 递归下载共享或目录：

`smbget --recursive {{smb://server/share}}`

- 使用用户名和密码连接：

`smbget {{smb://server/share/file}} --user {{username%password}}`

- 要求加密传输：

`smbget {{smb://server/share/file}} --encrypt`
