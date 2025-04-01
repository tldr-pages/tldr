# pmap

> 报告进程或多个进程的内存映射。
> 更多信息：<https://manned.org/pmap>.

- 打印特定进程ID（PID）的内存映射：

`pmap {{pid}}`

- 显示扩展格式：

`pmap --extended {{pid}}`

- 显示设备格式：

`pmap --device {{pid}}`

- 将结果限制在由 `low` 和 `high` 指定的内存地址范围内：

`pmap --range {{low}},{{high}}`

- 打印多个进程的内存映射：

`pmap {{pid1 pid2 ...}}`