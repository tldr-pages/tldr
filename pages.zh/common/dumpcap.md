# dumpcap

> 网络流量抓取工具。
> 更多信息：<https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- 显示可用的网络接口：

`dumpcap --list-interfaces`

- 在指定的网络接口上抓取数据包：

`dumpcap --interface {{1}}`

- 将数据包捕获到指定位置：

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}}`

- 将数据写入环形缓冲区，设置特定大小的最大文件限制和文件数量：

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}} --ring-buffer filesize:{{500000}} --ring-buffer files:{{10}}`