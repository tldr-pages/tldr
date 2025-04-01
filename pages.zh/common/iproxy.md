# iproxy

> 将本地 TCP 端口绑定到 USB 设备上的指定端口的代理。
> 更多信息：<https://manned.org/iproxy>.

- 将本地 TCP 端口绑定并转发到已连接的 USB 设备上的端口：

`iproxy {{local_port}}:{{device_port}}`

- 将多个本地 TCP 端口绑定并转发到已连接的 USB 设备上的相应端口：

`iproxy {{local_port1}}:{{device_port1}} {{local_port2}}:{{device_port2}}`

- 将本地端口绑定并转发到特定设备（通过 UDID 指定）：

`iproxy --udid {{device_udid}} {{local_port}}:{{device_port}}`

- 将本地端口绑定并转发到启用了 WiFi 同步的网络连接设备：

`iproxy --network {{local_port}}:{{device_port}}`
