# l2ping

> 发送 L2CAP 回声请求并接收响应。
> 更多信息：<https://manned.org/l2ping>。

- Ping 一个蓝牙设备：

`sudo l2ping {{mac_address}}`

- 反向 Ping 一个蓝牙设备：

`sudo l2ping -r {{mac_address}}`

- 从指定接口 Ping 一个蓝牙设备：

`sudo l2ping -i {{hci0}} {{mac_address}}`

- 用指定大小的数据包 Ping 蓝牙设备：

`sudo l2ping -s {{byte_count}} {{mac_address}}`

- 对蓝牙设备进行 Ping 洪水攻击：

`sudo l2ping -f {{mac_address}}`

- 指定次数 Ping 一个蓝牙设备：

`sudo l2ping -c {{amount}} {{mac_address}}`

- 以指定延迟 Ping 一个蓝牙设备：

`sudo l2ping -d {{seconds}} {{mac_address}}`