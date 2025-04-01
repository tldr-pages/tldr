# gdb

> GNU 调试器。
> 更多信息：<https://www.gnu.org/software/gdb>。

- 调试可执行文件：

`gdb {{executable}}`

- 将进程附加到 gdb：

`gdb {{[-p|--pid]}} {{procID}}`

- 使用核心文件调试：

`gdb {{[-c|--core]}} {{core}} {{executable}}`

- 启动时执行给定的 GDB 命令：

`gdb {{[-ex|--eval-command]}} "{{commands}}" {{executable}}`

- 启动 `gdb` 并将参数传递给可执行文件：

`gdb --args {{executable}} {{argument1}} {{argument2}}`

- 跳过 debuginfod 和分页提示，然后打印调用栈：

`gdb {{[-c|--core]}} {{core}} {{executable}} -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt`
