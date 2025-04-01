# chrt

> 操纵进程的实时属性。
> 更多信息：<https://manned.org/chrt>.

- 显示进程的属性：

`chrt {{[-p|--pid]}} {{PID}}`

- 显示进程所有线程的属性：

`chrt {{[-a|--all-tasks]}} {{[-p|--pid]}} {{PID}}`

- 显示 `chrt` 可用的最小/最大优先级值：

`chrt {{[-m|--max]}}`

- 设置进程的调度优先级：

`chrt {{[-p|--pid]}} {{priority}} {{PID}}`

- 设置进程的调度策略：

`chrt --{{deadline|idle|batch|rr|fifo|other}} {{[-p|--pid]}} {{priority}} {{PID}}`
