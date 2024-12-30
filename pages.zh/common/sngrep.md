# sngrep

> 从终端显示SIP呼叫消息流。
> 更多信息：<https://github.com/irontec/sngrep>。

- 从PCAP文件可视化SIP数据包：

`sngrep -I {{path/to/file.pcap}}`

- 仅可视化以INVITE数据包开始的对话和来自PCAP文件的RTP数据包：

`sngrep -crI {{path/to/file.pcap}}`

- 实时接口，仅显示以INVITE数据包开始的对话和RTP数据包：

`sngrep -cr`

- 仅捕获数据包，不通过接口保存到文件：

`sngrep -NO {{path/to/file.pcap}}`