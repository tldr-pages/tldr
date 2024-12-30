# dmesg

> 将内核消息写入 `stdout`。
> 更多信息：<https://manned.org/dmesg>。

- 显示内核消息：

`sudo dmesg`

- 显示内核错误消息：

`sudo dmesg --level err`

- 显示内核消息并持续读取新消息，类似于 `tail -f`（在内核 3.5.0 及更高版本中可用）：

`sudo dmesg -w`

- 显示此系统上可用的物理内存：

`sudo dmesg | grep -i memory`

- 每次显示一页内核消息：

`sudo dmesg | less`

- 显示带时间戳的内核消息（在内核 3.5.0 及更高版本中可用）：

`sudo dmesg -T`

- 以人类可读的形式显示内核消息（在内核 3.5.0 及更高版本中可用）：

`sudo dmesg -H`

- 着色输出（在内核 3.5.0 及更高版本中可用）：

`sudo dmesg -L`