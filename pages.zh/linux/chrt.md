# chrt

> 操作进程的实时属性。
> 更多信息：<https://manned.org/chrt>。

- 显示进程的属性：

`chrt --pid {{PID}}`

- 显示进程所有线程的属性：

`chrt --all-tasks --pid {{PID}}`

- 显示可以与 `chrt` 一起使用的最小/最大优先级值：

`chrt --max`

- 设置进程的调度优先级：

`chrt --pid {{priority}} {{PID}}`

- 设置进程的调度策略：

`chrt --{{deadline|idle|batch|rr|fifo|other}} --pid {{priority}} {{PID}}`