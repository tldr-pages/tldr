# ltrace

> 显示进程的动态库调用。
> 更多信息：<https://manned.org/ltrace>。

- 打印（跟踪）程序二进制文件的库调用：

`ltrace ./{{程序}}`

- 统计库调用。在底部打印一个方便的摘要：

`ltrace -c {{路径/到/程序}}`

- 跟踪对 malloc 和 free 的调用，省略由 libc 进行的调用：

`ltrace -e malloc+free-@libc.so* {{路径/到/程序}}`

- 写入文件而不是终端：

`ltrace -o {{文件}} {{路径/到/程序}}`