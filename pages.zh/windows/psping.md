# psping

> 一个包含 TCP Ping、延迟和带宽测量功能的 Ping 工具。
> 更多信息：<https://learn.microsoft.com/sysinternals/downloads/psping>。

- 使用 ICMP Ping 一个主机：

`psping {{hostname}}`

- 通过 TCP 端口 Ping 一个主机：

`psping {{hostname}}:{{port}}`

- 指定 Ping 的次数并安静地执行：

`psping {{hostname}} -n {{pings}} -q`

- 通过 TCP 端口 Ping 目标 50 次并生成结果的直方图：

`psping {{hostname}}:{{port}} -q -n {{50}} -h`

- 显示帮助信息：

`psping /?`