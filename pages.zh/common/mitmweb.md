# mitmweb

> 基于 Web 的交互式中间人 HTTP 代理。
> 参见：`mitmproxy`。
> 更多信息：<https://docs.mitmproxy.org/stable/concepts-options>。

- 使用默认设置启动 `mitmweb`：

`mitmweb`

- 将 `mitmweb` 绑定到自定义地址和端口启动：

`mitmweb --listen-host {{ip_address}} --listen-port {{port}}`

- 使用脚本处理流量启动 `mitmweb`：

`mitmweb --scripts {{path/to/script.py}}`
