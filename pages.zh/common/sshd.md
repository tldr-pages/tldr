# sshd

> 安全 Shell 守护进程，允许远程机器安全登录当前机器。
> 远程机器可以像在当前机器上一样执行命令。
> 更多信息：<https://man.openbsd.org/sshd>。

- 在后台启动守护进程：

`sshd`

- 在前台运行 sshd：

`sshd -D`

- 使用详细输出运行（用于调试）：

`sshd -D -d`

- 在特定端口上运行：

`sshd -p {{端口}}`
