# whatwaf

> 检测并绕过网络应用防火墙和保护系统。
> 更多信息：<https://github.com/Ekultek/WhatWaf>。

- 检测单个 [u]RL 的保护，可选使用详细输出：

`whatwaf --url {{https://example.com}} --verbose`

- 从文件中并行检测 [l]ist 中的 URL 保护（每行一个 URL）：

`whatwaf --threads {{number}} --list {{path/to/file}}`

- 通过代理发送请求，并使用来自文件的自定义有效负载列表（每行一个有效负载）：

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{path/to/file}} -u {{https://example.com}}`

- 通过 Tor 发送请求（必须安装 Tor），使用自定义 [p]ayloads（以逗号分隔）：

`whatwaf --tor --payloads '{{payload1,payload2,...}}' -u {{https://example.com}}`

- 使用随机用户代理，设置限流和超时，发送 [P]OST 请求，并强制使用 HTTPS 连接：

`whatwaf --ra --throttle {{seconds}} --timeout {{seconds}} --post --force-ssl -u {{http://example.com}}`

- 列出所有可以检测到的 WAF：

`whatwaf --wafs`

- 列出所有可用的篡改脚本：

`whatwaf --tampers`