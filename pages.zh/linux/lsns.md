# lsns

> 列出所有命名空间或指定命名空间的信息。
> 更多信息：<https://manned.org/lsns>.

- 列出所有命名空间：

`lsns`

- 以 JSON 格式列出命名空间：

`lsns {{[-J|--json]}}`

- 列出与指定进程关联的命名空间：

`lsns {{[-p|--task]}} {{pid}}`

- 仅列出指定类型的命名空间：

`lsns {{[-t|--type]}} {{mnt|net|ipc|user|pid|uts|cgroup|time}}`

- 列出命名空间，仅显示命名空间 ID、类型、PID 和命令：

`lsns {{[-o|--output]}} {{NS,TYPE,PID,COMMAND}}`
