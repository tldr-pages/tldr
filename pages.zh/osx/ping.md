# ping

> 向网络主机发送 ICMP ECHO_REQUEST 数据包。
> 更多信息：<https://keith.github.io/xcode-man-pages/ping.8.html>。

- Ping 指定的主机：

`ping "{{hostname}}"`

- Ping 主机指定次数：

`ping -c {{count}} "{{host}}"`

- Ping 主机，指定请求之间的间隔（默认是 1 秒）：

`ping -i {{seconds}} "{{host}}"`

- Ping 主机，不尝试查找地址的符号名称：

`ping -n "{{host}}"`

- Ping 主机并在接收到数据包时响铃（如果你的终端支持）：

`ping -a "{{host}}"`

- Ping 主机并打印接收到数据包的时间（此选项为 Apple 的附加功能）：

`ping --apple-time "{{host}}"`
