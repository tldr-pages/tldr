# trace-cmd

> 用于与 Ftrace Linux 内核内部追踪器交互的工具。
> 此工具仅以 root 身份运行。
> 更多信息：<https://manned.org/trace-cmd>。

- 显示追踪系统的状态：

`trace-cmd stat`

- 列出可用的追踪器：

`trace-cmd list -t`

- 使用特定插件开始追踪：

`trace-cmd start -p {{timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop}}`

- 查看追踪输出：

`trace-cmd show`

- 停止追踪但保留缓冲区：

`trace-cmd stop`

- 清除追踪缓冲区：

`trace-cmd clear`

- 清除追踪缓冲区并停止追踪：

`trace-cmd reset`