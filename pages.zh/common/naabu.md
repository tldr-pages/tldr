# naabu

> 一个用 Go 编写的快速端口扫描器，注重可靠性和简单性。
> 注意：某些功能仅在使用根权限运行 `naabu` 时激活，例如 SYN 扫描。
> 更多信息：<https://github.com/projectdiscovery/naabu>。

- 对远程主机的默认（前 100 个）端口进行 SYN 扫描：

`sudo naabu -host {{host}}`

- 显示可用的网络接口和本地主机的公共 IP 地址：

`naabu -interface-list`

- 扫描远程主机的所有端口（无需 `sudo` 的 CONNECT 扫描）：

`naabu -p - -host {{host}}`

- 扫描远程主机的前 1000 个端口：

`naabu -top-ports 1000 -host {{host}}`

- 扫描远程主机的 TCP 端口 80、443 和 UDP 端口 53：

`naabu -p 80,443,u:53 -host {{host}}`

- 显示远程主机使用的 CDN 类型（如果有的话）：

`naabu -p 80,443 -cdn -host {{host}}`

- 从 `naabu` 运行 `nmap` 以获得额外功能（必须安装 `nmap`）：

`sudo naabu -v -host {{host}} -nmap-cli 'nmap {{-v -T5 -sC}}'`