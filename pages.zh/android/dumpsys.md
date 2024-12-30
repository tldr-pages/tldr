# dumpsys

> 获取关于Android系统服务的信息。
> 此命令只能通过`adb shell`使用。
> 更多信息：<https://developer.android.com/tools/dumpsys>。

- 获取所有系统服务的诊断输出：

`dumpsys`

- 获取特定系统服务的诊断输出：

`dumpsys {{service}}`

- 列出`dumpsys`可以提供信息的所有服务：

`dumpsys -l`

- 列出特定服务的服务参数：

`dumpsys {{service}} -h`

- 从诊断输出中排除特定服务：

`dumpsys --skip {{service}}`

- 指定超时时间（单位：秒，默认为10秒）：

`dumpsys -t {{8}}`