# ipaggcreate

> 生成 TCP/IP 数据包转储的聚合统计信息。
> 更多信息：<https://manned.org/ipaggcreate>.

- 统计 PCAP 文件中每个源地址发送的数据包数量：

`ipaggcreate --src {{path/to/file.pcap}}`

- 按 IP 数据包长度分组并统计从网络接口读取的数据包数量：

`ipaggcreate --interface {{eth0}} --length`

- 统计 PCAP 文件中每对地址之间传输的字节数量：

`ipaggcreate --address-pairs --bytes {{path/to/file.pcap}}`
