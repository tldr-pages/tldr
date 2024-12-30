# sa

> 汇总用户调用的命令的会计信息，包括处理所花费的 CPU 时间和 I/O 速率的基本信息。
> 属于 `acct` 包的一部分。
> 更多信息：<https://manned.org/sa.8>。

- 显示每个用户的可执行调用次数（不显示用户名）：

`sudo sa`

- 显示每个用户的可执行调用次数，显示负责的用户名：

`sudo sa --print-users`

- 列出最近每个用户使用的资源：

`sudo sa --user-summary`