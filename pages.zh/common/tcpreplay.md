# tcpreplay

> 重放存储在 `pcap` 文件中的网络流量。
> 更多信息：<https://tcpreplay.appneta.com/>.

- 列出可用的网络接口：

`tcpreplay --listnics`

- 将流量重放到接口：

`tcpreplay -i {{eth0}} {{traffic.pcap}}`

- 将流量重放到接口并输出到 `stdout`：

`tcpreplay -i {{eth0}} --verbose {{traffic.pcap}}`

- 尽可能快地将流量重放到接口：

`tcpreplay -i {{eth0}} --topspeed {{traffic.pcap}}`

- 以给定的 Mbps 将流量重放到接口：

`tcpreplay -i {{eth0}} -M {{10}} {{traffic.pcap}}`

- 将流量重放到接口若干次：

`tcpreplay -i {{eth0}} --loop={{num_times}} {{traffic.pcap}}`