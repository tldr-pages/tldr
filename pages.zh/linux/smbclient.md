# smbclient

> 用于访问服务器上的 SMB/CIFS 资源的类似 FTP 的客户端。
> 更多信息：<https://manned.org/smbclient>。

- 连接到一个共享资源（用户将被提示输入密码；输入 `exit` 退出会话）：

`smbclient {{//server/share}}`

- 使用不同用户名连接：

`smbclient {{//server/share}} --user {{username}}`

- 使用不同的工作组连接：

`smbclient {{//server/share}} --workgroup {{domain}} --user {{username}}`

- 使用用户名和密码连接：

`smbclient {{//server/share}} --user {{username%password}}`

- 从服务器下载文件：

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "get {{file.txt}}"`

- 上传文件到服务器：

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "put {{file.txt}}"`

- 匿名列出服务器上的共享资源：

`smbclient --list={{server}} --no-pass`
