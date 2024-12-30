# taskkill

> 通过进程 ID 或名称终止一个进程。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>。

- 通过进程 ID 终止一个进程：

`taskkill /pid {{process_id}}`

- 通过进程名称终止一个进程：

`taskkill /im {{process_name}}`

- 强制终止指定的进程：

`taskkill /pid {{process_id}} /f`

- 终止一个进程及其子进程：

`taskkill /im {{process_name}} /t`

- 在远程计算机上终止一个进程：

`taskkill /pid {{process_id}} /s {{remote_name}}`

- 显示命令使用信息：

`taskkill /?`