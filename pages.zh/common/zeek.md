# zeek

> 被动网络流量分析器。
> 所有输出和日志文件将保存到当前工作目录。
> 更多信息：<https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- 分析来自网络接口的实时流量：

`sudo zeek --iface {{接口}}`

- 分析来自网络接口的实时流量并加载自定义脚本：

`sudo zeek --iface {{接口}} {{脚本1}} {{脚本2}}`

- 分析来自网络接口的实时流量，不加载任何脚本：

`sudo zeek --bare-mode --iface {{接口}}`

- 分析来自网络接口的实时流量，应用 `tcpdump` 过滤器：

`sudo zeek --filter {{路径/到/过滤器}} --iface {{接口}}`

- 使用看门狗计时器分析来自网络接口的实时流量：

`sudo zeek --watchdog --iface {{接口}}`

- 分析来自 PCAP 文件的流量：

`zeek --readfile {{路径/到/文件.trace}}`
