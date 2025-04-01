# tcpdump

> 捕获网络中的流量。
> 更多信息：<https://www.tcpdump.org>。

- 列出可用的网络接口：

`tcpdump {{[-D|--list-interfaces]}}`

- 捕获特定接口的流量：

`sudo tcpdump {{[-i|--interface]}} {{eth0}}`

- 捕获所有 TCP 流量并在控制台中显示内容（ASCII）：

`tcpdump -A tcp`

- 捕获来自或发往特定主机的流量：

`tcpdump host {{www.example.com}}`

- 捕获来自特定接口、源地址、目的地址和目的端口的流量：

`sudo tcpdump {{[-i|--interface]} {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- 捕获特定网络的流量：

`tcpdump net {{192.168.1.0/24}}`

- 捕获除端口 22 之外的所有流量并保存到抓包文件中：

`tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- 从指定的抓包文件中读取：

`tcpdump -r {{dumpfile.pcap}}`