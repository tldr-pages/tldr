# sshd

> 安全壳守护进程 - 允许远程机器安全地登录到当前机器。
> 远程机器可以在当前机器上执行命令。
> 更多信息：<https://man.openbsd.org/sshd>.

- 在后台启动守护进程：

`sshd`

- 在前台运行 sshd：

`sshd -D`

- 以详细输出模式运行（用于调试）：

`sshd -D -d`

- 在特定端口上运行：

`sshd -p {{port}}`