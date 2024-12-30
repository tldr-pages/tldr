# torsocks

> 通过 Tor 网络路由任何应用程序的流量。
> 注意：`torsocks` 默认假设应该连接到运行在 127.0.0.1:9050 的 Tor SOCKS 代理，这是 Tor 守护进程的默认设置。
> 更多信息：<https://gitlab.torproject.org/tpo/core/torsocks/>.

- 使用 Tor 运行命令：

`torsocks {{command}}`

- 在此 shell 中启用或禁用 Tor：

`. torsocks {{on|off}}`

- 创建一个新的启用 Tor 的 shell：

`torsocks --shell`

- 检查当前 shell 是否启用 Tor（如果禁用，`LD_PRELOAD` 的值将为空）：

`torsocks show`

- [i]通过不同的 Tor 电路隔离流量，提高匿名性：

`torsocks --isolate {{curl https://check.torproject.org/api/ip}}`

- 连接到运行在特定 [a]ddress 和 [P]ort 的 Tor 代理：

`torsocks --address {{ip}} --port {{port}} {{command}}`