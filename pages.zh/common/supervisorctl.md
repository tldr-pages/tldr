# supervisorctl

> Supervisor 是一个客户端/服务器系统，允许用户控制类 Unix 操作系统上的多个进程。
> supervisorctl 是 Supervisor 的命令行客户端部分，提供类似 shell 的界面。
> 更多信息：<http://supervisord.org>。

- 显示进程的状态（如果未指定 `process_name`，则显示所有进程的状态）：

`supervisorctl status {{process_name}}`

- 启动/停止/重启一个进程：

`supervisorctl {{start|stop|restart}} {{process_name}}`

- 启动/停止/重启某个组中的所有进程：

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- 显示进程 `stderr` 的最后 100 字节：

`supervisorctl tail -100 {{process_name}} stderr`

- 持续显示进程的 `stdout`：

`supervisorctl tail -f {{process_name}} stdout`

- 重新加载进程配置文件以根据需要添加或删除进程：

`supervisorctl update`
