# log

> 查看、导出和配置日志系统。
> 更多信息：<https://keith.github.io/xcode-man-pages/log.1.html>.

- 实时查看系统日志流：

`log stream`

- 查看来自特定 PID 进程的 syslog 日志流：

`log stream --process {{process_id}}`

- 查看来自特定名称进程的 syslog 日志：

`log show --predicate "process == '{{process_name}}'"`

- 导出过去一小时的所有日志到磁盘：

`sudo log collect --last {{1h}} --output {{path/to/file.logarchive}}`