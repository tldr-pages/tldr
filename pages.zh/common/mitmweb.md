# mitmweb

> 一个基于网络的交互式中间人HTTP代理。
> 另请参见：`mitmproxy`。
> 更多信息：<https://docs.mitmproxy.org/stable/concepts-options>。

- 使用默认设置启动 `mitmweb`：

`mitmweb`

- 启动 `mitmweb` 并绑定到自定义地址和端口：

`mitmweb --listen-host {{ip_address}} --listen-port {{port}}`

- 使用脚本处理流量启动 `mitmweb`：

`mitmweb --scripts {{path/to/script.py}}`