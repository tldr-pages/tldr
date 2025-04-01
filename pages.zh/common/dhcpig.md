# dhcpig

> 发起高级的 DHCP 耗竭攻击和压力测试。
> 必须以 root 权限运行 DHCPig。
> 更多信息：<https://github.com/kamorin/DHCPig>。

- 使用指定接口耗尽所有可用的 DHCP 地址：

`sudo ./pig.py {{eth0}}`

- 使用 eth1 接口耗尽 IPv6 地址：

`sudo ./pig.py -6 {{eth1}}`

- 使用指定接口发送模糊/畸形的数据包：

`sudo ./pig.py --fuzz {{eth1}}`

- 启用彩色输出：

`sudo ./pig.py -c {{eth1}}`

- 启用最小详细程度和彩色输出：

`sudo ./pig.py -c --verbosity=1 {{eth1}}`

- 设置调试详细程度为 100 并使用 ARP 数据包扫描邻近设备的网络：

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp {{eth1}}`

- 启用打印租约信息，尝试扫描并释放所有邻近 IP 地址：

`sudo ./pig.py --neighbors-scan-arp -r --show-options {{eth1}}`
