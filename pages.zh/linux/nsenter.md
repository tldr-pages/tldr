# nsenter

> 在正在运行的进程的名称空间中运行新命令。
> 对于 Docker 镜像或 chroot 监狱特别有用。
> 更多信息：<https://manned.org/nsenter>。

- 使用与现有进程相同的名称空间运行特定命令：

`nsenter --target {{pid}} --all {{command}} {{command_arguments}}`

- 在现有进程的挂载|UTS|IPC|网络|PID|用户|cgroup|时间名称空间中运行特定命令：

`nsenter --target {{pid}} --{{mount|uts|ipc|net|pid|user|cgroup}} {{command}} {{command_arguments}}`

- 在现有进程的 UTS、时间和 IPC 名称空间中运行特定命令：

`nsenter --target {{pid}} --uts --time --ipc -- {{command}} {{command_arguments}}`

- 通过引用 procfs 在现有进程的名称空间中运行特定命令：

`nsenter --pid=/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`