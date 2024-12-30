# ncat

> 在网络上读取、写入、重定向和加密数据。
> 一种类似工具 `netcat`/`nc` 的替代实现。
> 更多信息：<https://nmap.org/ncat/guide/index.html>。

- 在指定端口上监听输入并将其写入指定文件：

`ncat -l {{port}} > {{path/to/file}}`

- 接受多个连接并在它们关闭后保持 ncat 打开：

`ncat -lk {{port}}`

- 将指定文件的输出写入指定主机的指定端口：

`ncat {{address}} {{port}} < {{path/to/file}}`

- 在加密通道上接受多个传入连接，规避流量内容的检测：

`ncat --ssl -k -l {{port}}`

- 通过 SSL 连接到一个开放的 `ncat` 连接：

`ncat --ssl {{host}} {{port}}`

- 在特定端口检查与远程主机的连接性并设置超时：

`ncat -w {{seconds}} -vz {{host}} {{port}}`