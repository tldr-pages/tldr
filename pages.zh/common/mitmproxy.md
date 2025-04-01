# mitmproxy

> 一个互动的中间人HTTP代理。
> 参见：`mitmweb` 和 `mitmdump`。
> 更多信息：<https://docs.mitmproxy.org/stable/>。

- 使用默认设置启动 `mitmproxy`（将监听8080端口）：

`mitmproxy`

- 绑定到自定义地址和端口启动 `mitmproxy`：

`mitmproxy --listen-host {{ip_address}} {{[-p|--listen-port]}} {{port}}`

- 使用脚本处理流量启动 `mitmproxy`：

`mitmproxy {{[-s|--scripts]}} {{path/to/script.py}}`

- 将带有SSL/TLS主密钥的日志导出到外部程序（如wireshark等）：

`SSLKEYLOGFILE="{{path/to/file}}" mitmproxy`

- 指定代理服务器的操作模式（`regular` 是默认模式）：

`mitmproxy {{[-m|--mode]}} {{regular|transparent|socks5|...}}`

- 设置控制台布局：

`mitmproxy --console-layout {{horizontal|single|vertical}}`