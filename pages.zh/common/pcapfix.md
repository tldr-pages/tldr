# pcapfix

> 修复损坏或 corrupted 的 PCAP 和 PcapNG 文件。
> 更多信息：<https://f00l.de/pcapfix/>.

- 修复 PCAP/PcapNG 文件（注意：对于 PCAP 文件，只会扫描每个数据包的前 262144 字节）：

`pcapfix {{path/to/file.pcapng}}`

- 修复整个 PCAP 文件：

`pcapfix --deep-scan {{path/to/file.pcap}}`

- 修复 PCAP/PcapNG 文件并将修复后的文件写入指定位置：

`pcapfix --outfile {{path/to/repaired.pcap}} {{path/to/file.pcap}}`

- 将指定文件视为 PcapNG 文件，忽略自动识别：

`pcapfix --pcapng {{path/to/file.pcapng}}`

- 修复文件并详细显示过程：

`pcapfix --verbose {{path/to/file.pcap}}`