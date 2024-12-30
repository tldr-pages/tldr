# cryptcat

> Cryptcat 是具有加密功能的 netcat。
> 更多信息请访问：<https://cryptcat.sourceforge.net>。

- 在指定的端口上[l]isten并打印接收到的任何数据：

`cryptcat -k {{密码}} -l -p {{端口}}`

- 连接到某个端口：

`cryptcat -k {{密码}} {{ip地址}} {{端口}}`

- 指定超时时间（[w]）：

`cryptcat -k {{密码}} -w {{超时时间（秒）}} {{ip地址}} {{端口}}`

- 扫描（[z]）指定主机的开放端口：

`cryptcat -v -z {{ip地址}} {{端口}}`

- 充当代理，将数据从本地 TCP 端口转发到给定的远程主机：

`cryptcat -k {{密码}} -l -p {{本地端口}} | cryptcat -k {{密码}} {{主机名}} {{远程端口}}`