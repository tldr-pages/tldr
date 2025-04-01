# lldb

> LLVM 低级调试器。
> 更多信息：<https://lldb.llvm.org>。

- 调试一个可执行文件：

`lldb {{executable}}`

- 附加 `lldb` 到指定 PID 的正在运行的进程：

`lldb -p {{pid}}`

- 等待指定名称的新进程启动，并附加到该进程：

`lldb -w -n {{process_name}}`