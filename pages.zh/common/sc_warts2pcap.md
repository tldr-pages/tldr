# sc_warts2pcap

> 将 `warts` 对象中的数据包写入 PCAP 文件。
> 这仅适用于 tbit、sting 和 sniff。
> 更多信息请访问: <https://www.caida.org/catalog/software/scamper/>.

- 将多个 `warts` 文件中的数据转换为一个 PCAP 文件：

`sc_warts2pcap -o {{path/to/output.pcap}} {{path/to/file1.warts path/to/file2.warts ...}}`

- 将 `warts` 文件中的数据转换为 PCAP 文件，并按时间戳对数据包进行排序：

`sc_warts2pcap -s -o {{path/to/output.pcap}} {{path/to/file.warts}}`