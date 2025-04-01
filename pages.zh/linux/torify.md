# torify

> 通过 Tor 网络路由网络流量。
> 注意：此命令已弃用，现在是 `torsocks` 的向后兼容包装器。
> 更多信息：<https://manned.org/torify>.

- 通过 Tor 路由流量：

`torify {{command}}`

- 在 shell 中切换 Tor：

`torify {{on|off}}`

- 启动一个启用了 Tor 的 shell：

`torify --shell`

- 检查是否启用了 Tor 的 shell：

`torify show`

- 指定 Tor 配置文件：

`torify -c {{config-file}} {{command}}`

- 使用特定的 Tor SOCKS 代理：

`torify -P {{proxy}} {{command}}`

- 将输出重定向到文件：

`torify {{command}} > {{path/to/output}}`