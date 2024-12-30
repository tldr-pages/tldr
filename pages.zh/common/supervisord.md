# supervisord

> Supervisor 是一个用于控制 UNIX 类操作系统上某些进程的客户端/服务器系统。
> Supervisord 是 Supervisor 的服务器部分；它主要通过配置文件进行管理。
> 更多信息：<http://supervisord.org>。

- 使用指定的配置文件启动 `supervisord`：

`supervisord -c {{path/to/file}}`

- 在前台运行 supervisord：

`supervisord -n`