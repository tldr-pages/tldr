# sc_ttlexp

> 从 `warts` 文件中的 ICMP TTL 过期消息中提取源地址。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>.

- 依次输出 `warts` 文件中 ICMP TTL 过期消息的源地址：

`sc_ttlexp {{path/to/file1.warts path/to/file2.warts ...}}`