# ipsumdump

> 将 TCP/IP 数据包转储总结为人类和机器可读的 ASCII 格式。
> 更多信息：<https://manned.org/ipsumdump>.

- 打印 PCAP 文件中所有数据包的源和目标 IP 地址：

`ipsumdump --src --dst {{path/to/file.pcap}}`

- 打印从指定网络接口读取的所有数据包的时间戳、源地址、源端口、目标地址、目标端口和协议：

`ipsumdump --interface {{eth0}} -tsSdDp`

- 打印 PCAP 文件中所有数据包的匿名化源地址、匿名化目标地址和 IP 数据包长度：

`ipsumdump --src --dst --length --anonymize {{path/to/file.pcap}}`
