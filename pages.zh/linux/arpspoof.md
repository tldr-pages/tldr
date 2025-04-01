# arpspoof

> 伪造 ARP 回复以拦截数据包。
> 更多信息：<https://manned.org/arpspoof>。

- 毒化所有主机以拦截指定接口上的数据包：

`sudo arpspoof -i {{wlan0}} {{host_ip}}`

- 毒化指定目标以拦截指定接口上的数据包：

`sudo arpspoof -i {{wlan0}} -t {{target_ip}} {{host_ip}}`

- 毒化目标和主机以拦截指定接口上的数据包：

`sudo arpspoof -i {{wlan0}} -r -t {{target_ip}} {{host_ip}}`