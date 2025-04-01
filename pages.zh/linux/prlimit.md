# prlimit

> 获取或设置进程资源的软限制和硬限制。
> 给定一个进程 ID 和一个或多个资源，prlimit 尝试检索和/或修改这些限制。
> 更多信息：<https://manned.org/prlimit>.

- 显示当前运行父进程的所有资源的限制值：

`prlimit`

- 显示指定进程的所有当前资源的限制值：

`prlimit {{[-p|--pid]}} {{pid_number}}`

- 以自定义的打开文件数量限制运行命令：

`prlimit {{[-n|--nofile=]}}{{10}} {{command}}`