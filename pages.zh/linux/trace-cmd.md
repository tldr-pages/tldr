# trace-cmd

> 用于与 Ftrace 内核内部跟踪器交互的工具。
> 该工具仅能以 root 身份运行。
> 更多信息：<https://manned.org/trace-cmd>。

- 显示跟踪系统的状态：

`trace-cmd stat`

- 列出可用的跟踪器：

`trace-cmd list -t`

- 使用特定插件开始跟踪：

`trace-cmd start -p {{timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop}}`

- 查看跟踪输出：

`trace-cmd show`

- 停止跟踪但保留缓冲区：

`trace-cmd stop`

- 清除跟踪缓冲区：

`trace-cmd clear`

- 清除跟踪缓冲区并停止跟踪：

`trace-cmd reset`
