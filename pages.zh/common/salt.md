# salt

> 在远程的 Salt minion 上执行命令和断言状态。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/index.html>.

- 列出已连接的 minion：

`salt '*' test.ping`

- 在所有已连接的 minion 上执行 highstate：

`salt '*' state.highstate`

- 在一部分 minion 上使用操作系统包管理器（如 apt, yum, brew）升级包：

`salt '*.example.com' pkg.upgrade`

- 在特定的 minion 上执行任意命令：

`salt '{{minion_id}}' cmd.run "ls "`
