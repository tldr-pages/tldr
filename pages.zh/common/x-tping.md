# x tping

> TCP 端口 Ping。
> 该模块基于 TCP 协议，使用 curl 实现本地计算机到目标主机和端口的简单明文 TCP 连接。
> 更多信息：<https://x-cmd.com/mod/tping>。

- 使用详细模式 Ping 主机的 80 端口（默认端口）：

`x tping {{host}}`

- Ping 指定主机的特定端口：

`x tping {{host}}:{{port}}`

- 以热力图形式显示结果：

`x tping --heatmap {{host}}`

- 以柱状图形式显示结果：

`x tping --bar {{host}}:{{port}}`

- 以原始数据模式输出：

`x tping --raw {{host}}`

- 以 CSV 格式输出：

`x tping --csv {{host}}`

- 以 TSV 格式输出：

`x tping --tsv {{host}}`
