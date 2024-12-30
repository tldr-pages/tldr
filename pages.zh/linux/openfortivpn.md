# openfortivpn

> 一个用于Fortinet专有PPP+SSL VPN解决方案的VPN客户端。
> 更多信息：<https://github.com/adrienverge/openfortivpn>。

- 使用用户名和密码连接到VPN：

`openfortivpn --username={{username}} --password={{password}}`

- 使用特定的配置文件连接到VPN（默认为`/etc/openfortivpn/config`）：

`sudo openfortivpn --config={{path/to/config}}`

- 通过指定主机和端口连接到VPN：

`openfortivpn {{host}}:{{port}}`

- 通过传递其证书的sha256摘要来信任给定的网关：

`openfortivpn --trusted-cert={{sha256_sum}}`