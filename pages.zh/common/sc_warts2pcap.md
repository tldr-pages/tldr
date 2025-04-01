# sc_warts2pcap

> 将 `warts` 对象中包含的数据包写入到一个 PCAP 文件。
> 这只适用于 tbit、sting 和 sniff。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>.

- 将多个 `warts` 文件中的数据转换为一个 PCAP 文件：

`sc_warts2pcap -o {{path/to/output.pcap}} {{path/to/file1.warts path/to/file2.warts ...}}`

- 将 `warts` 文件中的数据转换为 PCAP 文件，并按时间戳排序数据包：

`sc_warts2pcap -s -o {{path/to/output.pcap}} {{path/to/file.warts}}`