# tasklist

> 显示本地或远程计算机上当前正在运行的进程的列表。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- 显示当前正在运行的进程：

`tasklist`

- 使用指定的格式显示当前进程列表：

`tasklist /fo {{table|list|csv}}`

- 已匹配的方式（.exe, .dll）显示当前运行的进程：

`tasklist /m {{匹配模式}}`

- 显示在远程计算机上运行的进程：

`tasklist /s {{远程主机名}} /u {{用户名}} /p {{密码}}`

- 显示每个进程中的服务信息：

`tasklist /svc`
