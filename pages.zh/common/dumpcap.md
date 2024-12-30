# dumpcap

> 一个网络流量捕获工具。
> 更多信息：<https://www.wireshark.org/docs/man-pages/dumpcap.html>。

- 显示可用的接口：

`dumpcap --list-interfaces`

- 在特定接口上捕获数据包：

`dumpcap --interface {{1}}`

- 将数据包捕获到特定位置：

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}}`

- 以特定的最大文件限制和特定大小写写入环形缓冲区：

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}} --ring-buffer filesize:{{500000}} --ring-buffer files:{{10}}`