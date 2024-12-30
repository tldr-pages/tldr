# flock

> 从 shell 脚本管理锁。
> 它可以用来确保一个命令只有一个进程在运行。
> 更多信息：<https://manned.org/flock>。

- 当锁不被其他进程占用时，立即以文件锁运行命令：

`flock {{path/to/lock.lock}} --command "{{command}}"`

- 以文件锁运行命令，如果锁不存在则退出：

`flock {{path/to/lock.lock}} --nonblock --command "{{command}}"`

- 以文件锁运行命令，如果锁不存在则以特定错误代码退出：

`flock {{path/to/lock.lock}} --nonblock --conflict-exit-code {{error_code}} -c "{{command}}"`
