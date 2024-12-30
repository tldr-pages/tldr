# sslstrip

> 执行 Moxie Marlinspike 的安全套接字层 (SSL) 去除攻击。
> 配合进行 ARP 欺骗攻击。
> 更多信息：<https://www.kali.org/tools/sslstrip/>.

- 默认情况下，仅记录端口 10000 上的 HTTPS POST 流量：

`sslstrip`

- 仅记录端口 8080 上的 HTTPS POST 流量：

`sslstrip --listen={{8080}}`

- 记录所有往返于服务器的 SSL 流量，端口 8080：

`sslstrip --ssl --listen={{8080}}`

- 记录所有往返于服务器的 SSL 和 HTTP 流量，端口 8080：

`sslstrip --listen={{8080}} --all`

- 指定存储日志的文件路径：

`sslstrip --listen={{8080}} --write={{path/to/file}}`

- 显示帮助信息：

`sslstrip --help`