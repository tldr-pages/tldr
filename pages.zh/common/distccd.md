# distccd

> distcc 分布式编译器的服务器守护进程。
> 更多信息：<https://distcc.github.io>。

- 使用默认设置启动守护进程：

`distccd --daemon`

- 启动一个守护进程，接受来自 IPv4 私有网络范围的连接：

`distccd --daemon --allow-private`

- 启动一个守护进程，接受来自特定网络地址或地址范围的连接：

`distccd --daemon --allow {{ip_address|network_prefix}}`

- 启动一个优先级降低的守护进程，最多可以同时运行 4 个任务：

`distccd --daemon --jobs {{4}} --nice {{5}}`

- 启动一个守护进程，并通过 mDNS/DNS-SD (Zeroconf) 注册它：

`distccd --daemon --zeroconf`