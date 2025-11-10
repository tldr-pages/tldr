# bpftool

> 以简单的方式检查和操作 eBPF 程序和映射。
> 某些子命令（如 `prog`）有各自的用法文档。
> 更多信息：<https://manned.org/bpftool>.

- 列出已加载的 `eBPF` 程序信息：

`bpftool prog list`

- 列出内核网络子系统中的 `eBPF` 程序附件：

`bpftool net list`

- 列出所有活动链接：

`bpftool link list`

- 列出系统中所有的 raw_tracepoint、tracepoint、kprobe 附件：

`bpftool perf list`

- 列出 BPF 类型格式（BTF）数据：

`bpftool btf list`

- 列出已加载映射的信息：

`bpftool map list`

- 探测网络设备 "eth0" 支持的 eBPF 功能：

`bpftool feature probe dev {{eth0}}`

- 从文件以批处理模式运行命令：

`bpftool batch file {{文件}}`
