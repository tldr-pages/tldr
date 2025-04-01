# hping3

> 高级 ping 工具，支持 TCP、UDP 和原始 IP 协议。
> 最好以提升的权限运行。
> 更多信息：<https://github.com/antirez/hping>.

- 使用 4 次 ICMP 请求 ping 目标地址：

`hping3 --icmp --count {{4}} {{ip_or_hostname}}`

- 通过 UDP 协议在 80 端口 ping IP 地址：

`hping3 --udp --destport {{80}} --syn {{ip_or_hostname}}`

- 扫描 80 端口的 TCP，从特定的本地源端口 5090 开始扫描：

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}`

- 使用 TCP 扫描进行 traceroute 到特定的目标端口：

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_or_hostname}}`

- 扫描特定 IP 地址的一组 TCP 端口：

`hping3 --scan {{80,3000,9000}} --syn {{ip_or_hostname}}`

- 执行 TCP ACK 扫描以检查特定主机是否在线：

`hping3 --count {{2}} --verbose --destport {{80}} --ack {{ip_or_hostname}}`

- 在 80 端口执行洪水测试：

`hping3 --flood --destport {{80}} --syn {{ip_or_hostname}}`