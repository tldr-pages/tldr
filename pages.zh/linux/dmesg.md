# dmesg

> 显示或控制内核环形缓冲区。
> 更多信息：<https://manned.org/dmesg>.

- 显示来自内核环形缓冲区的所有消息：

`sudo dmesg`

- 只显示严重错误级别的消息：

`sudo dmesg {{[-l|--level]}} err`

- 等待新消息。仅在具有可读性的系统上支持此功能，类似于 `tail -f`（从内核 3.5.0 版本开始）：

`sudo dmesg {{[-w|--follow]}}`

- 显示此系统上有多少物理内存可用：

`sudo dmesg | grep {{[-i|--ignore-case]}} memory`

- 以分页方式显示内核缓冲区的所有消息：

`sudo dmesg | less`

- 打印人类可读的时间戳（从内核 3.5.0 版本开始）：

`sudo dmesg {{[-T|--ctime]}}`

- 启用人类可读的输出：

`sudo dmesg {{[-H|--human]}}`

- 着色输出：

`sudo dmesg {{[-L|--color]}}`
