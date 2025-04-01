# procstat

> 显示 FreeBSD 中进程的详细信息。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- 显示特定进程的文件描述符：

`procstat fds {{pid}}`

- 显示进程的虚拟内存映射：

`procstat vm {{pid}}`

- 显示进程的参数：

`procstat arguments {{pid}}`

- 显示进程的资源限制：

`procstat rlimit {{pid}}`
