# ipsumdump

> 将 TCP/IP 数据包汇总为人类和机器可读的 ASCII 格式。
> 更多信息：<https://manned.org/ipsumdump>。

- 打印 PCAP 文件中所有数据包的源和目的 IP 地址：

`ipsumdump --src --dst {{path/to/file.pcap}}`

- 打印从给定网络接口读取的所有数据包的时间戳、源地址、源端口、目的地址、目的端口和协议：

`ipsumdump --interface {{eth0}} -tsSdDp`

- 打印 PCAP 文件中所有数据包的匿名源地址、匿名目的地址和 IP 数据包长度：

`ipsumdump --src --dst --length --anonymize {{path/to/file.pcap}}`