# ncat

> 在网络上读取、写入、重定向和加密数据。
> `netcat`/`nc` 的替代实现。
> 更多信息：<https://nmap.org/ncat/guide/index.html>。

- 监听指定端口上的输入并将其写入指定文件：

`ncat -l {{port}} > {{path/to/file}}`

- 接受多个连接并在连接关闭后保持 ncat 打开：

`ncat -lk {{port}}`

- 将指定文件的输出写入指定主机的指定端口：

`ncat {{address}} {{port}} < {{path/to/file}}`

- 在加密通道上接受多个传入连接以避免流量内容被检测：

`ncat --ssl -k -l {{port}}`

- 通过 SSL 连接到开放的 ncat 连接：

`ncat --ssl {{host}} {{port}}`

- 使用超时检查到远程主机特定端口的连通性：

`ncat -w {{seconds}} -vz {{host}} {{port}}`
