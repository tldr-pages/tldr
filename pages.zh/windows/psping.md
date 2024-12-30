# psping

> 一个包括 TCP ping、延迟和带宽测量的 ping 工具。
> 更多信息：<https://learn.microsoft.com/sysinternals/downloads/psping>。

- 使用 ICMP ping 一个主机：

`psping {{hostname}}`

- 通过 TCP 端口 ping 一个主机：

`psping {{hostname}}:{{port}}`

- 指定 ping 的次数并静默执行：

`psping {{hostname}} -n {{pings}} -q`

- 通过 TCP 对目标进行 50 次 ping，并生成结果的直方图：

`psping {{hostname}}:{{port}} -q -n {{50}} -h`

- 显示帮助信息：

`psping /?`