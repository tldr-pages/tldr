# resolveip

> 将主机名解析为其IP地址，反之亦然。
> 更多信息：<https://mariadb.com/kb/en/resolveip/>。

- 将主机名解析为IP地址：

`resolveip {{example.org}}`

- 将IP地址解析为主机名：

`resolveip {{1.1.1.1}}`

- 静默模式。输出更少：

`resolveip --silent {{example.org}}`