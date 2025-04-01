# pw-top

> 实时查看 PipeWire 节点和设备的统计信息。
> 相关命令：`pipewire`, `pw-dump`, `pw-cli`, `pw-profiler`。
> 更多信息：<https://docs.pipewire.org/page_man_pw-top_1.html>。

- 显示 PipeWire 节点和设备的交互式视图：

`pw-top`

- 监控远程实例：

`pw-top --remote {{remote_name}}`

- 以非交互模式定期打印信息，而非运行在交互模式：

`pw-top --batch-mode`

- 以非交互模式定期打印信息，指定次数：

`pw-top --batch-mode --iterations {{3}}`
