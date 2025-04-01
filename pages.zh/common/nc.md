# nc

> 通过这个多功能工具将 I/O 重定向到网络流中。
> 更多信息：<https://manned.org/nc>.

- 在指定的 TCP 端口启动监听器，并将文件发送到监听器：

`nc -l -p {{port}} < {{filename}}`

- 连接到指定端口的目标监听器，并从它接收文件：

`nc {{host}} {{port}} > {{received_filename}}`

- 扫描指定主机的开放 TCP 端口：

`nc -v -z -w {{timeout_in_seconds}} {{host}} {{start_port}}-{{end_port}}`

- 在指定的 TCP 端口启动监听器，并为连接方提供本地 shell 访问（这很危险，可能会被滥用）：

`nc -l -p {{port}} -e {{shell_executable}}`

- 连接到目标监听器，并为远程方提供本地 shell 访问（这很危险，可能会被滥用）：

`nc {{host}} {{port}} -e {{shell_executable}}`

- 作为代理，将本地 TCP 端口的数据转发到指定的远程主机：

`nc -l -p {{local_port}} | nc {{host}} {{remote_port}}`

- 发送 HTTP GET 请求：

`echo -e "GET / HTTP/1.1\nHost: {{host}}\n\n" | nc {{host}} 80`
