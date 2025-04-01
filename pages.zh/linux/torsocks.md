# torsocks

> 将任何应用程序的流量通过 Tor 网络路由。
> 注意：`torsocks` 默认会连接到运行在 127.0.0.1:9050 的 Tor SOCKS 代理，这是 Tor 守护进程的默认设置。
> 更多信息：<https://manned.org/torsocks>.

- 使用 Tor 运行命令：

`torsocks {{command}}`

- 在此 shell 中启用或禁用 Tor：

`. torsocks {{on|off}}`

- 启动一个新的 Tor 已启用的 shell：

`torsocks --shell`

- 检查当前 shell 是否已启用 Tor（如果未启用，`LD_PRELOAD` 值将为空）：

`torsocks show`

- 通过不同的 Tor 电路隔离流量，以提高匿名性：

`torsocks {{[-i|--isolate]}} {{curl https://check.torproject.org/api/ip}}`

- 连接到特定地址和端口上的 Tor 代理：

`torsocks {{[-a|--address]}} {{ip}} {{[-P|--port]}} {{port}} {{command}}`