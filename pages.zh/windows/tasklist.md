# 任务列表

> 显示本地或远程计算机上当前正在运行的进程列表。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>。

- 显示当前正在运行的进程：

`tasklist`

- 以指定的输出格式显示运行的进程：

`tasklist /fo {{table|list|csv}}`

- 使用指定的 `.exe` 或 `.dll` 文件名显示运行的进程：

`tasklist /m {{module_pattern}}`

- 显示在远程计算机上运行的进程：

`tasklist /s {{remote_name}} /u {{username}} /p {{password}}`

- 显示每个进程使用的服务：

`tasklist /svc`