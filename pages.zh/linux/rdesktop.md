# rdesktop

> 远程桌面协议客户端。
> 可以使用 RDP 协议连接到远程计算机。
> 更多信息：<https://manned.org/rdesktop>。

- 连接到远程计算机（默认端口为 3389）：

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- 简单示例：

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- 连接到远程计算机并全屏显示（按 `<Ctrl Alt Enter>` 退出）：

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- 使用自定义分辨率（数字之间使用 'x' 分隔）：

`rdesktop -u {{username}} -p {{password}} -g 1366x768 {{host:port}}`

- 使用域用户连接到远程计算机：

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- 使用 16 位颜色（加速）：

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`