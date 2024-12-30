# nping

> 网络数据包生成工具/ping 实用程序。
> 更多信息：<https://nmap.org/nping/>.

- 使用 ICMP 对指定主机进行 ping，如果用户被允许的话，否则使用 TCP：

`nping {{example.com}}`

- 假设用户被允许，使用 ICMP 对指定主机进行 ping：

`nping --icmp --privileged {{example.com}}`

- 使用 UDP 对指定主机进行 ping：

`nping --udp {{example.com}}`

- 使用 TCP 对指定主机的给定端口进行 ping：

`nping --tcp --dest-port {{443}} {{example.com}}`

- ping 指定次数：

`nping --count {{10}} {{example.com}}`

- 在每次 ping 之间等待一定时间：

`nping --delay {{5s}} {{example.com}}`

- 通过指定接口发送请求：

`nping --interface {{eth0}} {{example.com}}`

- ping 一个 IP 范围：

`nping {{10.0.0.1-10}}`