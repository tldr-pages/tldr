# x tping

> 通过 TCP 协议 ping 主机以检查其可达性。
> 更多信息：<https://x-cmd.com/mod/tping>。

- 使用详细模式 Ping 主机的 80 端口（默认端口）：

`x tping {{host}}`

- Ping 指定主机的特定端口：

`x tping {{host}}:{{port}}`

- 以热力图形式显示结果：

`x tping {{[-m|--heatmap]}} {{host}}`

- 以柱状图形式显示结果：

`x tping {{[-b|--bar]}} {{host}}:{{port}}`

- 输出原始数据：

`x tping {{[-r|--raw]}} {{host}}`

- 输出指定格式：

`x tping {{--csv|--tsv}} {{host}}`
