# lldb

> LLVM低级调试器。
> 更多信息：<https://lldb.llvm.org>。

- 调试一个可执行文件：

`lldb {{可执行文件}}`

- 将`lldb`附加到一个具有给定PID的运行中的进程：

`lldb -p {{pid}}`

- 等待以给定名称启动的新进程，并附加到它：

`lldb -w -n {{进程名称}}`