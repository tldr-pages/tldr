# ionice

> 获取或设置程序的 I/O 调度类和优先级。
> 调度类：1（实时），2（最佳努力），3（空闲）。
> 优先级级别：0（最高） - 7（最低）。
> 更多信息：<https://manned.org/ionice>。

- 以给定的调度类和优先级运行命令：

`ionice -c {{scheduling_class}} -n {{priority}} {{command}}`

- 设置特定 [p]id、[P]gid 或 [u]id 的正在运行进程的 I/O 调度[c]lass：

`ionice -c {{scheduling_class}} -{{p|P|u}} {{id}}`

- 以自定义的 I/O 调度[c]lass 和优先级运行命令：

`ionice -c {{scheduling_class}} -n {{priority}} {{command}}`

- 忽略设置请求优先级失败的情况：

`ionice -t -n {{priority}} -p {{pid}}`

- 即使无法设置所需的优先级也运行命令（这可能是由于权限不足或旧内核版本导致的）：

`ionice -t -n {{priority}} -p {{pid}}`

- 打印正在运行进程的 I/O 调度类和优先级：

`ionice -p {{pid}}`