# arpspoof

> 伪造 ARP 响应以拦截数据包。
> 更多信息：<https://monkey.org/~dugsong/dsniff>。

- 通过接口对所有主机进行投毒，以拦截主机的数据包：

`sudo arpspoof -i {{wlan0}} {{host_ip}}`

- 通过接口对目标进行投毒，以拦截主机的数据包：

`sudo arpspoof -i {{wlan0}} -t {{target_ip}} {{host_ip}}`

- 同时对目标和主机进行投毒，以拦截主机的数据包：

`sudo arpspoof -i {{wlan0}} -r -t {{target_ip}} {{host_ip}}`