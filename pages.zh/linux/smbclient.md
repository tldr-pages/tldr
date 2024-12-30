# smbclient

> 类似FTP的客户端，用于访问服务器上的SMB/CIFS资源。
> 更多信息：<https://manned.org/smbclient>。

- 连接到共享（用户将被提示输入密码；使用`exit`退出会话）：

`smbclient {{//server/share}}`

- 使用不同的用户名连接：

`smbclient {{//server/share}} --user {{username}}`

- 使用不同的工作组连接：

`smbclient {{//server/share}} --workgroup {{domain}} --user {{username}}`

- 使用用户名和密码连接：

`smbclient {{//server/share}} --user {{username%password}}`

- 从服务器下载文件：

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "get {{file.txt}}"`

- 将文件上传到服务器：

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "put {{file.txt}}"`

- 匿名列出服务器上的共享：

`smbclient --list={{server}} --no-pass`