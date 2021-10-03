# taskkill

> 按进程 id 或进程名终止进程。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 通过进程 id 终止进程：

`taskkill /pid {{进程 id}}`

- 通过进程名终止进程：

`taskkill /im {{进程名}}`

- 强制终止一个指定的进程：

`taskkill /pid {{进程名}} /f`

- 终止一个进程及其子进程：

`taskkill /im {{进程名}} /t`

- 终止远程计算机上的进程：

`taskkill /pid {{进程 id}} /s {{远程主机名}}`

- 显示命令的帮助信息：

`taskkill /?`
