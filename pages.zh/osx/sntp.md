# sntp

> 一个非常简单的网络时间协议客户端程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/sntp.1>。

- 查询指定的 SNTP 服务器并显示时间：

`sntp {{pool.ntp.org}}`

- 将系统时钟与指定的 SNTP 服务器同步：

`sudo sntp -S {{pool.ntp.org}}`

- 启用调试日志：

`sntp -d {{pool.ntp.org}}`