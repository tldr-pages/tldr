# zeek

> 被动网络流量分析器。
> 所有输出和日志文件将保存到当前工作目录。
> 更多信息：<https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>。

- 从网络接口分析实时流量：

`sudo zeek --iface {{interface}}`

- 从网络接口分析实时流量并加载自定义脚本：

`sudo zeek --iface {{interface}} {{script1}} {{script2}}`

- 从网络接口分析实时流量，不加载任何脚本：

`sudo zeek --bare-mode --iface {{interface}}`

- 从网络接口分析实时流量，应用 `tcpdump` 过滤器：

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- 使用看门狗定时器从网络接口分析实时流量：

`sudo zeek --watchdog --iface {{interface}}`

- 从 PCAP 文件分析流量：

`zeek --readfile {{path/to/file.trace}}`