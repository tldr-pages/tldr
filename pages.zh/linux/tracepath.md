# tracepath

> 跟踪到网络主机的路径，发现沿途的最大传输单元（MTU）。
> 更多信息：<https://manned.org/tracepath>。

- 跟踪到主机的首选方式：

`tracepath -p {{33434}} {{host}}`

- 指定初始目标端口，在非标准防火墙设置中很有用：

`tracepath -p {{destination_port}} {{host}}`

- 同时打印主机名和数字IP地址：

`tracepath -b {{host}}`

- 指定最大生存时间（TTL，跳数）：

`tracepath -m {{max_hops}} {{host}}`

- 指定初始数据包长度（IPv4默认为65535，IPv6默认为128000）：

`tracepath -l {{packet_length}} {{host}}`

- 仅使用IPv6地址：

`tracepath -6 {{host}}`