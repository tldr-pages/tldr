# wmic

> 交互式 shell，用于获取正在运行的进程的详细信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- 基本语法：

`wmic {{别名}} {{where子句}} {{动词子句}}`

- 显示当前正在运行的进程的简要信息：

`wmic process list brief`

- 显示当前正在运行的进程的完整信息：

`wmic process list full`

- 访问特定字段，如进程名、进程 ID 和父进程 ID：

`wmic process get {{name,processid,parentprocessid}}`

- 显示特定进程的信息：

`wmic process where {{name="example.exe"}} list full`

- 显示特定进程的特定字段：

`wmic process where processid={{pid}} get {{name,commandline}}`

- 终止一个进程：

`wmic process {{pid}} delete`
