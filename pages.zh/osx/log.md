# 日志

> 查看、导出和配置日志系统。
> 更多信息：<https://keith.github.io/xcode-man-pages/log.1.html>。

- 实时流式传输系统日志：

`log stream`

- 从特定 PID 的进程中流式传输发送到 `syslog` 的日志：

`log stream --process {{process_id}}`

- 显示从特定名称的进程发送到 syslog 的日志：

`log show --predicate "process == '{{process_name}}'"`

- 将过去一小时的所有日志导出到磁盘：

`sudo log collect --last {{1h}} --output {{path/to/file.logarchive}}`