# rpcinfo

> 列出远程计算机上的 RPC 程序。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- 列出本地计算机上注册的所有程序：

`rpcinfo`

- 列出远程计算机上注册的所有程序：

`rpcinfo /p {{computer_name}}`

- 使用 TCP 在远程计算机上调用特定程序：

`rpcinfo /t {{computer_name}} {{program_name}}`

- 使用 UDP 在远程计算机上调用特定程序：

`rpcinfo /u {{computer_name}} {{program_name}}`
