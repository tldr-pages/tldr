# prctl

> 获取或设置正在运行的进程、任务和项目的资源控制。
> 更多信息：<https://www.unix.com/man-page/sunos/1/prctl>.

- 检查进程的限制和权限：

`prctl {{pid}}`

- 以机器可解析的格式检查进程的限制和权限：

`prctl -P {{pid}}`

- 获取正在运行的进程的特定限制：

`prctl -n process.max-file-descriptor {{pid}}`
