# flock

> 从 shell 脚本中管理锁。
> 它可以用来确保只有一个命令的进程在运行。
> 更多信息：<https://manned.org/flock>.

- 在锁不再被其他程序占用时，使用文件锁运行命令：

`flock {{path/to/lock.lock}} {{[-c|--command]}} "{{command}}"`

- 使用文件锁运行命令，如果锁不存在则退出：

`flock {{path/to/lock.lock}} {{[-n|--nonblock]}} {{[-c|--command]}} "{{command}}"`

- 使用文件锁运行命令，如果锁不存在则以特定的错误代码退出：

`flock {{path/to/lock.lock}} {{[-n|--nonblock]}} {{[-E|--conflict-exit-code]}} {{error_code}} {{[-c|--command]}} "{{command}}"`