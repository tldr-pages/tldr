# pio home

> 启动 PlatformIO Home 网页服务器。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>。

- 在默认的网页浏览器中打开 PlatformIO Home：

`pio home`

- 使用特定的 HTTP 端口（默认为 8008）：

`pio home --port {{port}}`

- 绑定到特定的 IP 地址（默认为 127.0.0.1）：

`pio home --host {{ip_address}}`

- 不自动在默认的网页浏览器中打开 PlatformIO Home：

`pio home --no-open`

- 当没有客户端连接时，在超时（以秒为单位）后自动关闭服务器：

`pio home --shutdown-timeout {{time}}`

- 指定一个唯一的会话标识符，以隔离其他实例并防止第三方访问：

`pio home --session-id {{id}}`
