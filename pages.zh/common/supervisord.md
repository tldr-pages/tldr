# supervisord

> Supervisor 是一个用于在类 Unix 操作系统上控制某些进程的客户端/服务器系统。
> supervisord 是 Supervisor 的服务器部分；主要通过配置文件进行管理。
> 更多信息：<http://supervisord.org>.

- 使用指定的配置文件启动 `supervisord`：

`supervisord -c {{path/to/file}}`

- 在前台运行 supervisord：

`supervisord -n`