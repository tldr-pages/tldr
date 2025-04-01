# wol

> 用于发送 Wake-on-LAN 魔法包的客户端。
> 更多信息：<https://sourceforge.net/projects/wake-on-lan/>.

- 向设备发送 WoL 包：

`wol {{mac_address}}`

- 基于 IP 地址向其他子网中的设备发送 WoL 包：

`wol --ipaddr={{ip_address}} {{mac_address}}`

- 基于主机名向其他子网中的设备发送 WoL 包：

`wol --host={{hostname}} {{mac_address}}`

- 向主机上的特定端口发送 WoL 包：

`wol --port={{port_number}} {{mac_address}}`

- 从文件中读取硬件地址、IP 地址/主机名、可选端口和 SecureON 密码：

`wol --file={{path/to/file}}`

- 开启详细输出：

`wol {{[-v|--verbose]}} {{mac_address}}`