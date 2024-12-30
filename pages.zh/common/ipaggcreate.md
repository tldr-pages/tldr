# ipaggcreate

> 生成 TCP/IP 转储的汇总统计信息。
> 更多信息：<https://manned.org/ipaggcreate>。

- 计算在 PCAP 文件中出现的每个源地址发送的包的数量：

`ipaggcreate --src {{path/to/file.pcap}}`

- 按 IP 包长度对从网络接口读取的包进行分组和计数：

`ipaggcreate --interface {{eth0}} --length`

- 计算在 PCAP 文件中出现的每对地址之间发送的字节数：

`ipaggcreate --address-pairs --bytes {{path/to/file.pcap}}`