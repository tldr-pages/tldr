# dhcpig

> 发起高级 DHCP 耗尽攻击和压力测试。
> DHCPig 需要以 root 权限运行。
> 更多信息：<https://github.com/kamorin/DHCPig>。

- 使用指定接口耗尽所有可用的 DHCP 地址：

`sudo ./pig.py {{eth0}}`

- 使用 eth1 接口耗尽 IPv6 地址：

`sudo ./pig.py -6 {{eth1}}`

- 使用接口发送模糊/损坏的数据包：

`sudo ./pig.py --fuzz {{eth1}}`

- 启用彩色输出：

`sudo ./pig.py -c {{eth1}}`

- 启用最小详细程度和彩色输出：

`sudo ./pig.py -c --verbosity=1 {{eth1}}`

- 使用 100 的调试详细程度，并使用 ARP 数据包扫描邻近设备的网络：

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp {{eth1}}`

- 启用打印租约信息，尝试扫描并释放所有邻近 IP 地址：

`sudo ./pig.py --neighbors-scan-arp -r --show-options {{eth1}}`