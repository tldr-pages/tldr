# rsh

> 在远程主机上执行命令。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- 在远程主机上执行命令：

`rsh {{remote_host}} {{ls -l}}`

- 使用特定用户名在远程主机上执行命令：

`rsh {{remote_host}} {{[-l|--user]}} {{username}} {{ls -l}}`

- 在远程主机上执行命令时将 `stdin` 重定向到 `/dev/null`：

`rsh {{remote_host}} --no-err {{ls -l}}`
