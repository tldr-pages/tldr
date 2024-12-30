# 日志输出

> 转储系统消息的日志，包括发生错误时的堆栈跟踪，以及应用程序记录的信息消息。
> 更多信息：<https://developer.android.com/tools/logcat>。

- 显示系统日志：

`logcat`

- 将系统日志写入一个[f]ile：

`logcat -f {{path/to/file}}`

- 显示匹配正则表达式的行：

`logcat --regex {{regular_expression}}`

- 显示特定PID的日志：

`logcat --pid {{pid}}`

- 显示特定包的进程日志：

`logcat --pid $(pidof -s {{package}})`