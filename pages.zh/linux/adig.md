# adig

> 打印从域名系统（DNS）服务器收到的信息。
> 更多信息：<https://manned.org/adig>.

- 显示主机名的 A 记录（默认记录）：

`adig {{example.com}}`

- 显示额外的 [d]ebugging 输出：

`adig -d {{example.com}}`

- 连接到特定的 DNS [s]erver：

`adig -s {{1.2.3.4}} {{example.com}}`

- 使用特定的 TCP 端口连接到 DNS 服务器：

`adig -T {{port}} {{example.com}}`

- 使用特定的 UDP 端口连接到 DNS 服务器：

`adig -U {{port}} {{example.com}}`
