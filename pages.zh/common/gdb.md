# gdb

> GNU 调试器。
> 更多信息：<https://www.gnu.org/software/gdb>。

- 调试可执行文件：

`gdb {{executable}}`

- 将进程附加到 gdb：

`gdb -p {{procID}}`

- 使用核心文件进行调试：

`gdb -c {{core}} {{executable}}`

- 启动时执行给定的 GDB 命令：

`gdb -ex "{{commands}}" {{executable}}`

- 启动 `gdb` 并传递参数给可执行文件：

`gdb --args {{executable}} {{argument1}} {{argument2}}`