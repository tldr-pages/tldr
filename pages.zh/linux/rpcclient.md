# rpcclient

> MS-RPC 客户端工具（samba 套件的一部分）。
> 更多信息：<https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>。

- 连接到远程主机：

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- 以无密码的方式连接到域上的远程主机：

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- 连接到远程主机，传递密码哈希：

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- 在远程主机上执行 shell 命令：

`rpcclient --user {{domain}}\{{username}}%{{password}} --command {{semicolon_separated_commands}} {{ip}}`

- 显示域用户：

`rpcclient $> enumdomusers`

- 显示权限：

`rpcclient $> enumprivs`

- 显示特定用户的信息：

`rpcclient $> queryuser {{username|rid}}`

- 在域中创建新用户：

`rpcclient $> createdomuser {{username}}`