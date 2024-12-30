# tcpdump

> 在网络上捕获流量。
> 更多信息：<https://www.tcpdump.org>。

- 列出可用的网络接口：

`tcpdump -D`

- 捕获特定接口的流量：

`tcpdump -i {{eth0}}`

- 捕获所有 TCP 流量并在控制台显示内容（ASCII）：

`tcpdump -A tcp`

- 捕获来自或发往主机的流量：

`tcpdump host {{www.example.com}}`

- 捕获特定接口、源、目的地和目的地端口的流量：

`tcpdump -i {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- 捕获一个网络的流量：

`tcpdump net {{192.168.1.0/24}}`

- 捕获所有流量，排除端口 22 的流量，并保存到转储文件中：

`tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- 从给定的转储文件中读取：

`tcpdump -r {{dumpfile.pcap}}`