# nping

> 网络数据包生成工具/ping 实用程序。
> 更多信息：<https://nmap.org/nping/>.

- 使用 ICMP（如果用户有权限）或者 TCP 来 ping 指定的主机：

`nping {{example.com}}`

- 假设用户有权限，使用 ICMP 来 ping 指定的主机：

`nping --icmp --privileged {{example.com}}`

- 使用 UDP 来 ping 指定的主机：

`nping --udp {{example.com}}`

- 在指定端口使用 TCP 来 ping 指定的主机：

`nping --tcp --dest-port {{443}} {{example.com}}`

- 指定 ping 的次数：

`nping --count {{10}} {{example.com}}`

- 每次 ping 之间等待指定的时间：

`nping --delay {{5s}} {{example.com}}`

- 通过指定的网络接口发送请求：

`nping --interface {{eth0}} {{example.com}}`

- ping 一个 IP 范围：

`nping {{10.0.0.1-10}}`