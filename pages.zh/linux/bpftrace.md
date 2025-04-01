# bpftrace

> Linux eBPF 的高级跟踪语言。
> 更多信息：<https://github.com/iovisor/bpftrace>.

- 显示 bpftrace 版本：

`bpftrace -V`

- 列出所有可用的探针：

`sudo bpftrace -l`

- 运行单行程序（例如按程序进行系统调用计数）：

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- 从文件运行程序：

`sudo bpftrace {{文件}}`

- 通过 PID 跟踪程序：

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- 进行试运行并以 eBPF 格式显示输出：

`sudo bpftrace -d -e '{{单行程序}}'`
