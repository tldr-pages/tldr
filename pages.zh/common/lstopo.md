# lstopo

> 显示系统的硬件拓扑结构。
> 更多信息：<https://manned.org/lstopo>.

- 在图形窗口中显示简化的系统拓扑结构（如果不可用图形显示，则在控制台中打印）：

`lstopo`

- 显示完整的系统拓扑结构，不进行简化：

`lstopo --no-factorize`

- 显示简化的系统拓扑结构，仅显示物理索引（即操作系统看到的）：

`lstopo {{[-p|--physical]}}`

- 将完整的系统拓扑结构以指定格式写入文件：

`lstopo --no-factorize {{[--of|--output-format]}} {{console|ascii|tex|fig|svg|pdf|ps|png|xml}} {{path/to/file}}`

- 以黑白或灰度模式输出：

`lstopo --palette {{none|grey}}`