# lstopo

> 显示系统的硬件拓扑。
> 更多信息：<https://manned.org/lstopo>。

- 在图形窗口中显示系统拓扑的摘要（如果没有图形显示则打印到控制台）：

`lstopo`

- 显示完整的系统拓扑而不进行摘要：

`lstopo --no-factorize`

- 仅显示带有 [p]hysical 索引的系统拓扑摘要（即操作系统所见）：

`lstopo --physical`

- 将完整的系统拓扑写入指定格式的文件：

`lstopo --no-factorize --output-format {{console|ascii|tex|fig|svg|pdf|ps|png|xml}} {{path/to/file}}`

- 以单色或灰度输出：

`lstopo --palette {{none|grey}}`