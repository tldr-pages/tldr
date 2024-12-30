# usbip

> 远程使用USB设备。
> 更多信息：<https://usbip.sourceforge.net>。

- 列出所有本地USB设备及其总线ID：

`usbip list --local`

- 在服务器上启动`usbip`守护进程：

`systemctl start usbipd`

- 在服务器上将USB设备绑定到`usbip`：

`sudo usbip bind --busid={{bus_id}}`

- 在客户端加载`usbip`所需的内核模块：

`sudo modprobe vhci-hcd`

- 在客户端连接到`usbip`设备（总线ID与服务器相同）：

`sudo usbip attach -r {{ip_address}} --busid={{bus_id}}`

- 列出已连接的设备：

`usbip port`

- 从设备中分离：

`sudo usbip detach --port={{port}}`

- 解绑设备：

`usbip unbind --busid={{bus_id}}`