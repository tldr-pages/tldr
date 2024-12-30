# 盐

> 在远程盐小鬼上执行命令并断言状态。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/index.html>。

- 列出已连接的小鬼：

`salt '*' test.ping`

- 在所有已连接的小鬼上执行高状态：

`salt '*' state.highstate`

- 在一部分小鬼上使用操作系统包管理器（apt、yum、brew）升级软件包：

`salt '*.example.com' pkg.upgrade`

- 在特定小鬼上执行任意命令：

`salt '{{minion_id}}' cmd.run "ls "`