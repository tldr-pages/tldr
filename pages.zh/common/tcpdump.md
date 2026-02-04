# tcpdump

> 转储网络上的流量。
> 更多信息：<https://www.tcpdump.org/manpages/tcpdump.1.html>。

- 列出所有可用的网络接口：

`tcpdump {{[-D|--list-interfaces]}}`

- 捕获特定网络接口的流量：

`sudo tcpdump {{[-i|--interface]}} {{eth0}}`

- 捕获所有 TCP 流量，并在控制台显示其内容（ASCII 编码）：

`sudo tcpdump -A tcp`

- 捕获发往或来自特定主机的流量：

`sudo tcpdump host {{www.example.com}}`

- 捕获来自特定接口、源、目的地且目的端口正确的流量：

`sudo tcpdump {{[-i|--interface]}} {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- 捕获特定网络的流量：

`sudo tcpdump net {{192.168.1.0/24}}`

- 捕获除 22 端口以外的所有流量，并写入转储文件：

`sudo tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- 从给定的转储文件中读取内容：

`tcpdump -r {{dumpfile.pcap}}`
