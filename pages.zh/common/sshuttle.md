# sshuttle

> 透明代理服务器，通过SSH连接隧道流量。
> 不需要在远程SSH服务器上拥有root权限或任何特殊设置，但在本地机器上会提示需要root访问权限。
> 更多信息：<https://manned.org/sshuttle>。

- 通过远程SSH服务器转发所有IPv4 TCP流量：

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- 还将所有DNS流量转发到服务器的默认DNS解析器：

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- 转发所有流量，但排除特定子网的流量：

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- 使用tproxy方法转发所有IPv4和IPv6流量：

`sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`