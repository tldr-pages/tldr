# tshark

> 数据包分析工具，Wireshark 的命令行版本。
> 更多信息：<https://tshark.dev/>.

- 监控本地主机上的所有流量：

`tshark`

- 仅捕获符合特定捕获过滤器的数据包：

`tshark -f '{{udp port 53}}'`

- 仅显示符合特定输出过滤器的数据包：

`tshark -Y '{{http.request.method == "GET"}}'`

- 使用特定协议（如 HTTP）解码 TCP 端口：

`tshark -d tcp.port=={{8888}},{{http}}`

- 指定捕获输出的格式：

`tshark -T {{json|text|ps|…}}`

- 选择特定字段输出：

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- 将捕获的数据包写入文件：

`tshark -w {{path/to/file}}`

- 分析来自文件的数据包：

`tshark -r {{path/to/file.pcap}}`