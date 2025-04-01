# trip

> 网络诊断工具。
> 结合了 `traceroute` 和 `ping` 的功能。
> 旨在帮助分析网络问题。
> 更多信息：<https://trippy.rs/>。

- 基本用法，使用默认参数：

`sudo trip {{example.com}}`

- 不需要提升权限的跟踪（仅支持某些平台）：

`trip {{example.com}} --unprivileged`

- 仅使用 `IPv6` 进行跟踪：

`sudo trip {{example.com}} --ipv6`

- 使用 `udp` 协议进行跟踪：

`sudo trip {{example.com}} --protocol {{udp}}`

- 使用自定义目标端口 `443` 进行 `tcp` 跟踪：

`sudo trip {{example.com}} --protocol {{tcp}} --target-port {{443}}`

- 使用自定义源端口 `5000` 进行 `udp` 跟踪：

`sudo trip {{example.com}} --protocol {{udp}} --source-port {{5000}}`
