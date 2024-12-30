# wmic

> 用于获取正在运行的进程的详细信息的交互式命令行。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>。

- 基本语法：

`wmic {{别名}} {{条件}} {{动词}}`

- 显示当前正在运行的进程的简要信息：

`wmic process list brief`

- 显示当前正在运行的进程的完整信息：

`wmic process list full`

- 访问特定字段，例如进程名称、进程 ID 和父进程 ID：

`wmic process get {{name,processid,parentprocessid}}`

- 显示特定进程的信息：

`wmic process where {{name="example.exe"}} list full`

- 显示特定进程的特定字段：

`wmic process where processid={{pid}} get {{name,commandline}}`

- 杀死一个进程：

`wmic process {{pid}} delete`