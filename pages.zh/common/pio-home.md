# pio home

> 启动 PlatformIO Home 网络服务器。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>。

- 在默认网页浏览器中打开 PlatformIO Home：

`pio home`

- 使用特定的 HTTP 端口（默认为 8008）：

`pio home --port {{port}}`

- 绑定到特定的 IP 地址（默认为 127.0.0.1）：

`pio home --host {{ip_address}}`

- 不自动在默认网页浏览器中打开 PlatformIO Home：

`pio home --no-open`

- 在没有客户端连接时，超时后自动关闭服务器（以秒为单位）：

`pio home --shutdown-timeout {{time}}`

- 指定一个唯一的会话标识符，以保持 PlatformIO Home 与其他实例隔离，并保护免受第三方访问：

`pio home --session-id {{id}}`