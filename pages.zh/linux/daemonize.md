# daemonize

> 将一个命令（不会自守护的命令）作为 Unix 守护进程运行。
> 更多信息：<https://software.clapper.org/daemonize/>。

- 作为守护进程运行一个命令：

`daemonize {{command}} {{command_arguments}}`

- 将 PID 写入指定文件：

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- 使用锁文件确保一次只运行一个实例：

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- 使用指定的用户账户：

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`
