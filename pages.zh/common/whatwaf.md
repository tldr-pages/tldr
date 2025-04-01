# whatwaf

> 检测和绕过 Web 应用防火墙及保护系统。
> 更多信息：<https://github.com/Ekultek/WhatWaf>.

- 检测单个 URL 的保护，可选使用详细输出：

`whatwaf {{[-u|--url]}} {{https://example.com}} --verbose`

- 并行检测文件中列出的 URL 列表（每行一个 URL）的保护：

`whatwaf {{[-t|--threads]}} {{number}} {{[-l|--list]}} {{path/to/file}}`

- 通过代理发送请求，并从文件中使用自定义负载列表（每行一个负载）：

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{path/to/file}} {{[-u|--url]}} {{https://example.com}}`

- 通过 Tor 发送请求（需要安装 Tor），使用自定义负载（逗号分隔）：

`whatwaf --tor {{[-p|--payloads]}} '{{payload1,payload2,...}}' {{[-u|--url]}} {{https://example.com}}`

- 使用随机用户代理，设置延时和超时，发送 POST 请求，并强制使用 HTTPS 连接：

`whatwaf --ra --throttle {{seconds}} --timeout {{seconds}} {{[-P|--post]}} --force-ssl {{[-u|--url]}} {{http://example.com}}`

- 列出所有可检测的 WAF：

`whatwaf --wafs`

- 列出所有可用的篡改脚本：

`whatwaf --tampers`