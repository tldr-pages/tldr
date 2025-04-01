# rexec

> 在远程主机上执行命令。
> 注意：使用 `rexec` 时要谨慎，因为它以明文形式传输数据。考虑使用如 SSH 等安全替代方案以实现加密通信。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- 在远程主机上执行命令：

`rexec {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- 指定远程主机上的用户名：

`rexec {{[-u|--username]}} {{username}} {{[-h|--host]}} {{remote_host}} {{ps aux}}`

- 从 `/dev/null` 重定向 `stdin` 到远程主机：

`rexec {{[-n|--noerr]}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- 指定远程主机上的端口：

`rexec {{[-P|--port]}} {{1234}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`
