# scamper

> 主动探测互联网以分析拓扑和性能。
> 包含一些以 `sc_` 开头的工具，例如 `sc_warts2text` 或 `sc_ttlexp`。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>。

- 执行标准选项（ traceroute ）到目标地址：

`scamper -i {{192.0.2.1}}`

- 对两个不同的目标执行两个操作（ ping 和 traceroute ）：

`scamper -I "{{ping}} {{192.0.2.1}}" -I "{{trace}} {{192.0.2.2}}"`

- 使用 UDP 对多个主机进行 ping 操作，为第一个 ping 指定端口号，并为后续的每个 ping 递增端口号：

`scamper -c "{{ping}} -P {{UDP-dport}} -d {{33434}}" -i {{192.0.2.1}} -i {{192.0.2.2}}`

- 使用多路径发现算法（ MDA ）确定到目标的负载均衡路径，并使用 ICMP 回显数据包进行采样，最多尝试三次，将结果写入 `warts` 文件：

`scamper -O {{warts}} -o {{path/to/output.warts}} -I "{{tracelb}} -P {{ICMP-echo}} -q {{3}} {{192.0.2.1}}"`

- 使用 ICMP 对目标执行 Paris traceroute 并将结果保存在压缩的 `warts` 文件中：

`scamper -O {{warts.gz}} -o {{path/to/output.warts}} -I "{{trace}} -P {{icmp-paris}} {{2001:db8:dead:beaf::4}}"`

- 记录到达特定 IP 地址且具有特定 ICMP ID 的所有 ICMP 数据包，并将它们保存在 `warts` 文件中：

`scamper -O {{warts}} -o {{path/to/output.warts}} -I "sniff -S {{2001:db8:dead:beef::6}} icmp[icmpid] == {{101}}"`