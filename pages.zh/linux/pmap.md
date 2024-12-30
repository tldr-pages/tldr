# pmap

> 报告一个或多个进程的内存映射。
> 更多信息：<https://manned.org/pmap>。

- 打印特定进程 ID (PID) 的内存映射：

`pmap {{pid}}`

- 显示扩展格式：

`pmap --extended {{pid}}`

- 显示设备格式：

`pmap --device {{pid}}`

- 将结果限制为由 `low` 和 `high` 指定的内存地址范围：

`pmap --range {{low}},{{high}}`

- 打印多个进程的内存映射：

`pmap {{pid1 pid2 ...}}`