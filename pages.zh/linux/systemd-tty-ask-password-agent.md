# systemd-tty-ask-password-agent

> 列出或处理待处理的 systemd 密码请求。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-tty-ask-password-agent.html>。

- 列出所有当前待处理的系统密码请求：

`systemd-tty-ask-password-agent --list`

- 持续处理密码请求：

`systemd-tty-ask-password-agent --watch`

- 通过在调用的 TTY 上询问用户来处理所有当前待处理的系统密码请求：

`systemd-tty-ask-password-agent --query`

- 将密码请求转发到 wall 而不是在调用的 TTY 上询问用户：

`systemd-tty-ask-password-agent --wall`
