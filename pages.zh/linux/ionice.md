# ionice

> 获取或设置程序的 I/O 调度类和优先级。
> 调度类：1（实时），2（尽力而为），3（空闲）。
> 优先级级别：0（最高）- 7（最低）。
> 更多信息：<https://manned.org/ionice>.

- 使用指定的调度类和优先级运行命令：

`ionice {{[-c|--class]}} {{scheduling_class}} {{[-n|--classdata]}} {{priority}} {{command}}`

- 设置指定 [p]id、[P]gid 或 [u]id 的运行进程的 I/O 调度类：

`ionice {{[-c|--class]}} {{scheduling_class}} -{{p|P|u}} {{id}}`

- 使用自定义的 I/O 调度类和优先级运行命令：

`ionice {{[-c|--class]}} {{scheduling_class}} {{[-n|--classdata]}} {{priority}} {{command}}`

- 忽略设置请求优先级失败的情况：

`ionice {{[-t|--ignore]}} {{[-n|--classdata]}} {{priority}} {{[-p|--pid]}} {{pid}}`

- 即使无法设置所需优先级（这可能是由于权限不足或内核版本过旧）也运行命令：

`ionice {{[-t|--ignore]}} {{[-n|--classdata]}} {{priority}} {{[-p|--pid]}} {{pid}}`

- 打印运行进程的 I/O 调度类和优先级：

`ionice {{[-p|--pid]}} {{pid}}`
