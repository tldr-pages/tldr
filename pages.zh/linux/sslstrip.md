# sslstrip

> 执行 Moxie Marlinspike 的 SSL 剥离攻击。
> 与 ARP 欺骗攻击结合使用。
> 更多信息：<https://www.kali.org/tools/sslstrip/>.

- 默认情况下仅记录 10000 端口上的 HTTPS POST 流量：

`sslstrip`

- 仅记录 8080 端口上的 HTTPS POST 流量：

`sslstrip --listen={{8080}}`

- 记录 8080 端口上与服务器之间的所有 SSL 流量：

`sslstrip --ssl --listen={{8080}}`

- 记录 8080 端口上与服务器之间的所有 SSL 和 HTTP 流量：

`sslstrip --listen={{8080}} --all`

- 指定存储日志的文件路径：

`sslstrip --listen={{8080}} --write={{path/to/file}}`

- 显示帮助：

`sslstrip --help`