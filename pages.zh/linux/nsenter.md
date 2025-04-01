# nsenter

> 在运行进程的命名空间中运行新命令。
> 特别适用于 Docker 镜像或 chroot 环境。
> 更多信息：<https://manned.org/nsenter>.

- 使用与现有进程相同的命名空间运行特定命令：

`nsenter {{[-t|--target]}} {{pid}} {{[-a|--all]}} {{command}} {{command_arguments}}`

- 在现有进程的 mount|UTS|IPC|network|PID|user|cgroup|time 命名空间中运行特定命令：

`nsenter {{[-t|--target]}} {{pid}} --{{mount|uts|ipc|net|pid|user|cgroup}} {{command}} {{command_arguments}}`

- 在现有进程的 UTS、time 和 IPC 命名空间中运行特定命令：

`nsenter {{[-t|--target]}} {{pid}} {{[-u|--uts]}} {{[-T|--time]}} {{[-i|--ipc]}} -- {{command}} {{command_arguments}}`

- 通过引用 procfs 在现有进程的命名空间中运行特定命令：

`nsenter {{[-p|--pid=]}}/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`