# sshpass

> SSH 密码提供程序。
> 它会创建一个 TTY，将密码输入其中，然后把 `stdin` 重定向到 SSH 会话。
> 更多信息：<https://manned.org/sshpass>。

- 使用通过文件描述符提供的密码连接到远程服务器（此例中为 `stdin`）：

`sshpass -d {{0}} ssh {{用户名}}@{{主机名}}`

- 使用作为选项提供的密码连接到远程服务器，并自动接受未知的 SSH 密钥：

`sshpass -p {{密码}} ssh -o StrictHostKeyChecking=no {{用户名}}@{{主机名}}`

- 使用文件第一行作为密码连接到远程服务器，自动接受未知的 SSH 密钥，并运行命令：

`sshpass -f {{路径/到/文件}} ssh -o StrictHostKeyChecking=no {{用户名}}@{{主机名}} "{{命令}}"`
