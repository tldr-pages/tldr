# sshpass

> SSH 密码提供工具。
> 它通过创建一个 TTY，将密码输入其中，然后将 `stdin` 重定向到 SSH 会话来工作。
> 更多信息：<https://manned.org/sshpass>。

- 使用从文件描述符（在本例中为 `stdin`）提供的密码连接到远程服务器：

`sshpass -d {{0}} ssh {{user}}@{{hostname}}`

- 使用作为选项提供的密码连接到远程服务器，并自动接受未知的 SSH 密钥：

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}`

- 使用文件的第一行作为密码连接到远程服务器，自动接受未知的 SSH 密钥，并启动一个命令：

`sshpass -f {{path/to/file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`