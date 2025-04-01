# ltrace

> 显示进程的动态库调用。
> 更多信息：<https://manned.org/ltrace>.

- 打印（跟踪）程序二进制文件的库调用：

`ltrace ./{{program}}`

- 统计库调用。在底部打印一个方便的摘要：

`ltrace -c {{path/to/program}}`

- 跟踪 malloc 和 free 的调用，省略 libc 完成的调用：

`ltrace -e malloc+free-@libc.so* {{path/to/program}}`

- 将输出写入文件而不是终端：

`ltrace -o {{file}} {{path/to/program}}`
