# l2ping

> 发送 L2CAP 回显请求并接收响应。
> 更多信息：<https://manned.org/l2ping>.

- 向蓝牙设备发送 ping 请求：

`sudo l2ping {{mac_address}}`

- 反向 ping 蓝牙设备：

`sudo l2ping -r {{mac_address}}`

- 从指定接口向蓝牙设备发送 ping 请求：

`sudo l2ping -i {{hci0}} {{mac_address}}`

- 使用指定大小的数据包向蓝牙设备发送 ping 请求：

`sudo l2ping -s {{byte_count}} {{mac_address}}`

- 洪泛 ping 蓝牙设备：

`sudo l2ping -f {{mac_address}}`

- 向蓝牙设备发送指定次数的 ping 请求：

`sudo l2ping -c {{amount}} {{mac_address}}`

- 以指定的请求间隔向蓝牙设备发送 ping 请求：

`sudo l2ping -d {{seconds}} {{mac_address}}`