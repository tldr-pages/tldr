# prlimit

> 获取或设置进程资源的软限制和硬限制。
> 给定一个进程ID和一个或多个资源，prlimit尝试检索和/或修改限制。
> 更多信息: <https://manned.org/prlimit>。

- 显示运行的父进程的所有当前资源的限制值：

`prlimit`

- 显示指定进程的所有当前资源的限制值：

`prlimit --pid {{pid_number}}`

- 使用自定义的打开文件限制运行命令：

`prlimit --nofile={{10}} {{command}}`