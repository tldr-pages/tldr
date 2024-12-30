# nc

> 通过这个多功能工具将输入/输出重定向到网络流中。
> 更多信息：<https://manned.org/nc>。

- 在指定的TCP端口上启动监听并将文件发送到其中：

`nc -l -p {{port}} < {{filename}}`

- 连接到指定端口的目标监听器并从中接收文件：

`nc {{host}} {{port}} > {{received_filename}}`

- 扫描指定主机的开放TCP端口：

`nc -v -z -w {{timeout_in_seconds}} {{host}} {{start_port}}-{{end_port}}`

- 在指定的TCP端口上启动监听并为连接方提供本地shell访问（这很危险，可能被滥用）：

`nc -l -p {{port}} -e {{shell_executable}}`

- 连接到目标监听器并为远程方提供本地shell访问（这很危险，可能被滥用）：

`nc {{host}} {{port}} -e {{shell_executable}}`

- 作为代理，将数据从本地TCP端口转发到给定的远程主机：

`nc -l -p {{local_port}} | nc {{host}} {{remote_port}}`

- 发送HTTP GET请求：

`echo -e "GET / HTTP/1.1\nHost: {{host}}\n\n" | nc {{host}} 80`