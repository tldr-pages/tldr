# sc_ttlexp

> 从 `warts` 文件中的 ICMP TTL 超时消息中提取源地址。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>.

- 逐个输出 `warts` 文件中 ICMP TTL 超时消息的源地址：

`sc_ttlexp {{路径/到/文件1.warts 路径/到/文件2.warts ...}}`