# unshare

> 在新的用户自定义命名空间中执行命令。
> 更多信息：<https://manned.org/unshare>.

- 不共享连接的网络资源，执行命令：

`unshare {{[-n|--net]}} {{command}} {{command_arguments}}`

- 作为子进程执行命令，不共享挂载点、进程或网络：

`unshare {{[-m|--mount]}} {{[-i|--pid]}} {{[-n|--net]}} {{[-f|--fork]}} {{command}} {{command_arguments}}`