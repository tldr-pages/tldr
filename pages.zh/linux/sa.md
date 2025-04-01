# sa

> 汇总用户调用命令的会计信息，包括处理所花费的CPU时间和I/O速率的基本信息。
> 是 `acct` 包的一部分。
> 更多信息：<https://manned.org/sa.8>.

- 显示每个用户的可执行文件调用（不显示用户名）：

`sudo sa`

- 显示每个用户的可执行文件调用，并显示负责的用户名：

`sudo sa --print-users`

- 列出每个用户最近使用的资源：

`sudo sa --user-summary`