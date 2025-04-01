# tcpreplay

> 重放存储在 `pcap` 文件中的网络流量。
> 更多信息：<https://tcpreplay.appneta.com/>.

- 列出可用的网络接口：

`tcpreplay --listnics`

- 重放流量到指定的网络接口：

`tcpreplay -i {{eth0}} {{traffic.pcap}}`

- 重放流量到指定的网络接口并输出到 `stdout`：

`tcpreplay -i {{eth0}} --verbose {{traffic.pcap}}`

- 尽可能快地重放流量到指定的网络接口：

`tcpreplay -i {{eth0}} --topspeed {{traffic.pcap}}`

- 以指定的 Mbps 重放流量到指定的网络接口：

`tcpreplay -i {{eth0}} -M {{10}} {{traffic.pcap}}`

- 重放流量到指定的网络接口多次：

`tcpreplay -i {{eth0}} --loop={{num_times}} {{traffic.pcap}}`