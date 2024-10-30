# logcat

> 转储系统消息日志，包括发生错误时的堆栈跟踪信息，以及应用程序记录的信息消息。
> 更多信息：<https://developer.android.com/tools/logcat>.

- 显示系统日志：

`logcat`

- 将系统日志写入文件（[f]ile）：

`logcat -f {{路径/到/文件}}`

- 显示与正则表达式匹配的日志行：

`logcat --regex {{正则表达式}}`

- 显示特定 PID 的日志：

`logcat --pid {{pid}}`

- 显示特定包的进程日志：

`logcat --pid $(pidof -s {{包}})`
