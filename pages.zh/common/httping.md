# httping

> 测量 Web 服务器的延迟和吞吐量。
> 更多信息：<https://manned.org/httping>。

- 指定 URL 进行 Ping 测试：

`httping -g {{url}}`

- 对 `host` 和 `port` 上的 Web 服务器进行 Ping 测试：

`httping -h {{host}} -p {{port}}`

- 使用 TLS 连接对 `host` 上的 Web 服务器进行 Ping 测试：

`httping -l -g https://{{host}}`

- 使用 HTTP 基本身份验证对 `host` 上的 Web 服务器进行 Ping 测试：

`httping -g http://{{host}} -U {{username}} -P {{password}}`
