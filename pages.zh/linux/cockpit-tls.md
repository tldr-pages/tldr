# cockpit-tls

> TLS 终止 HTTP 代理，用于加密客户端与 `cockpit-ws` 之间的流量。
> 更多信息：<https://cockpit-project.org/guide/latest/cockpit-tls.8.html>。

- 将 HTTP 请求服务到指定端口，而不是端口 `9090`：

`cockpit-tls --port {{port}}`

- 显示帮助信息：

`cockpit-tls --help`