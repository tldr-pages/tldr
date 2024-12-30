# daemonize

> 将一个命令（不自我守护的）作为 Unix 守护进程运行。
> 更多信息：<https://software.clapper.org/daemonize/>.

- 将命令作为守护进程运行：

`daemonize {{command}} {{command_arguments}}`

- 将 PID 写入指定文件：

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- 使用锁文件以确保一次只运行一个实例：

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- 使用指定的用户帐户：

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`