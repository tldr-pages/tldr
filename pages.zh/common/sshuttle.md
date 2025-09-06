# sshuttle

> 通过 SSH 连接传输流量的透明代理服务器。
> 不需要在远程 SSH 服务器上进行任何特殊设置，但会提示在本地机器上获取 root 访问权限。
> 更多信息：<https://manned.org/sshuttle>.

- 通过远程 SSH 服务器转发所有 IPv4 TCP 流量：

`sshuttle --remote={{用户名}}@{{服务器名}} {{0.0.0.0/0}}`

- 同时将所有 DNS 流量转发到服务器的默认 DNS 解析器：

`sshuttle --dns --remote={{用户名}}@{{服务器名}} {{0.0.0.0/0}}`

- 转发所有流量，除了发往特定子网的流量：

`sshuttle --remote={{用户名}}@{{服务器名}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- 使用 tproxy 方法转发所有 IPv4 和 IPv6 流量：

`sshuttle --method=tproxy --remote={{用户名}}@{{服务器名}} {{0.0.0.0/0}} {{::/0}} --exclude={{你本地 IP 地址}} --exclude={{SSH 服务器的 IP 地址}}`
