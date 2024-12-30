# bpftrace

> Linux eBPF的高级跟踪语言。
> 更多信息：<https://github.com/iovisor/bpftrace>。

- 显示bpftrace版本：

`bpftrace -V`

- 列出所有可用探针：

`sudo bpftrace -l`

- 运行一行程序（例如，通过程序的系统调用计数）：

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- 从文件运行程序：

`sudo bpftrace {{path/to/file}}`

- 按PID跟踪程序：

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- 进行干运行并以eBPF格式显示输出：

`sudo bpftrace -d -e '{{one_line_program}}'`