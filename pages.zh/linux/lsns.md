# lsns

> 列出所有命名空间的信息或指定命名空间的信息。
> 更多信息：<https://manned.org/lsns>。

- 列出所有命名空间：

`lsns`

- 以 JSON 格式列出命名空间：

`lsns --json`

- 列出与指定进程相关的命名空间：

`lsns --task {{pid}}`

- 仅列出指定类型的命名空间：

`lsns --type {{mnt|net|ipc|user|pid|uts|cgroup|time}}`

- 列出命名空间，仅显示命名空间 ID、类型、PID 和命令：

`lsns --output {{NS,TYPE,PID,COMMAND}}`