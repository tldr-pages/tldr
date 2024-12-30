# sshpass

> 一种 SSH 密码提供程序。
> 它通过创建一个 TTY，将密码输入其中，然后将 `stdin` 重定向到 SSH 会话来工作。
> 更多信息请访问：<https://manned.org/sshpass>。

- 使用在文件描述符中提供的密码（在此情况下为 `stdin`）连接到远程服务器：

`sshpass -d {{0}} ssh {{user}}@{{hostname}}`

- 使用作为选项提供的密码连接到远程服务器，并自动接受未知的 SSH 密钥：

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}`

- 使用文件的第一行作为密码连接到远程服务器，自动接受未知的 SSH 密钥，并启动一个命令：

`sshpass -f {{path/to/file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`