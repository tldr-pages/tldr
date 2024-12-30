# supervisorctl

> Supervisor 是一个客户端/服务器系统，允许用户在类 UNIX 操作系统上控制多个进程。
> Supervisorctl 是 Supervisor 的命令行客户端，提供类似于 shell 的界面。
> 更多信息请访问：<http://supervisord.org>。

- 显示进程状态（如果未指定 `process_name`，则显示所有进程）：

`supervisorctl status {{process_name}}`

- 启动/停止/重启进程：

`supervisorctl {{start|stop|restart}} {{process_name}}`

- 启动/停止/重启组中的所有进程：

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- 显示进程 `stderr` 的最后 100 字节：

`supervisorctl tail -100 {{process_name}} stderr`

- 持续显示进程的 `stdout`：

`supervisorctl tail -f {{process_name}} stdout`

- 重新加载进程配置文件，以根据需要添加/删除进程：

`supervisorctl update`