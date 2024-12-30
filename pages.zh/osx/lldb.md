# lldb

> LLVM 低级调试器。
> 更多信息：<https://lldb.llvm.org/man/lldb.html>。

- 调试一个可执行文件：

`lldb "{{executable}}"`

- 将 `lldb` 附加到具有给定 PID 的运行中进程：

`lldb -p {{pid}}`

- 等待以给定名称启动的新进程，并附加到它：

`lldb -w -n "{{process_name}}"`