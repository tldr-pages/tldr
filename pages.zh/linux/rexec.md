# rexec

> 在远程主机上执行命令。
> 注意：使用 `rexec` 时要谨慎，因为它以明文传输数据。考虑使用 SSH 等安全替代方案进行加密通信。
> 更多信息：<https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>。

- 在远程 [h]ost 上执行命令：

`rexec -h={{remote_host}} {{ls -l}}`

- 在远程 [h]ost 上指定远程 [u]sername：

`rexec -username={{username}} -h={{remote_host}} {{ps aux}}`

- 从远程 [h]ost 的 `/dev/null` 重定向 `stdin`：

`rexec --no-err -h={{remote_host}} {{ls -l}}`

- 在远程 [h]ost 上指定远程 [P]ort：

`rexec -P={{1234}} -h={{remote_host}} {{ls -l}}`