# lldb

> LLVM 低级调试器。
> 更多信息：<https://lldb.llvm.org/man/lldb.html>.

- 调试可执行文件：

`lldb "{{可执行的命令}}"`

- 将 `lldb` 附加到具有给定 PID 的正在运行的进程：

`lldb -p {{进程号 PID}}`

- 等待使用给定名称的进程启动，然后附加到该进程上：

`lldb -w -n "{{进程名}}"`
