# hping3

> 高级 ping 工具，支持 TCP、UDP 和原始 IP 等协议。
> 最好以提升的权限运行。
> 更多信息：<https://github.com/antirez/hping>。

- 使用 4 个 ICMP ping 请求 ping 一个目标：

`hping3 --icmp --count {{4}} {{ip_or_hostname}}`

- 在端口 80 上通过 UDP ping 一个 IP 地址：

`hping3 --udp --destport {{80}} --syn {{ip_or_hostname}}`

- 扫描 TCP 端口 80，从特定的本地源端口 5090 扫描：

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}`

- 使用 TCP 扫描进行 traceroute 到特定目标端口：

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_or_hostname}}`

- 在特定 IP 地址上扫描一组 TCP 端口：

`hping3 --scan {{80,3000,9000}} --syn {{ip_or_hostname}}`

- 执行 TCP ACK 扫描以检查给定主机是否存活：

`hping3 --count {{2}} --verbose --destport {{80}} --ack {{ip_or_hostname}}`

- 在端口 80 上执行压力测试：

`hping3 --flood --destport {{80}} --syn {{ip_or_hostname}}`