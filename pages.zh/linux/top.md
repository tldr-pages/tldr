# top

> 显示运行中的进程的动态实时信息。
> 更多信息：<https://manned.org/top>.

- 启动 `top`:

`top`

- 不显示任何空闲或僵尸进程:

`top {{[-i|--idle-toggle]}}`

- 仅显示指定用户的进程:

`top {{[-u|--filter-only-euser]}} {{username}}`

- 按字段排序进程:

`top {{[-o|--sort-override]}} {{field_name}}`

- 显示指定进程的各个线程:

`top {{[-Hp|--threads-show --pid]}} {{process_id}}`

- 仅显示具有给定 PID 的进程，以逗号分隔的列表形式传递。（通常你不会直接知道 PIDs。此示例从进程名称中选择 PIDs）:

`top {{[-p|--pid]}} $(pgrep {{[-d|--delimiter]}} ',' {{process_name}})`

- 显示交互命令的帮助:

`<?>`
