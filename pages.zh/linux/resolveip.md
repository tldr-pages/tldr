# resolveip

> 解析主机名到其 IP 地址，反之亦然。
> 更多信息：<https://mariadb.com/kb/en/resolveip/>.

- 将主机名解析为 IP 地址：

`resolveip {{example.org}}`

- 将 IP 地址解析为主机名：

`resolveip {{1.1.1.1}}`

- 静默模式。减少输出：

`resolveip --silent {{example.org}}`