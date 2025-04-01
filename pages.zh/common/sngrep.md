# sngrep

> 在终端显示 SIP 通话的消息流。
> 更多信息：<https://github.com/irontec/sngrep>。

- 从 PCAP 文件中可视化 SIP 数据包：

`sngrep -I {{path/to/file.pcap}}`

- 从 PCAP 文件中仅可视化以 INVITE 数据包开始并包含 RTP 数据包的对话：

`sngrep -crI {{path/to/file.pcap}}`

- 实时界面，仅显示以 INVITE 数据包开始并包含 RTP 数据包的对话：

`sngrep -cr`

- 仅捕获数据包而不通过界面保存到文件：

`sngrep -NO {{path/to/file.pcap}}`
