# openfortivpn

> 用于 Fortinet 专有 PPP+SSL VPN 解决方案的 VPN 客户端。
> 更多信息：<https://github.com/adrienverge/openfortivpn>.

- 使用用户名和密码连接到 VPN：

`openfortivpn --username={{username}} --password={{password}}`

- 使用特定配置文件连接到 VPN（默认为 `/etc/openfortivpn/config`）：

`sudo openfortivpn --config={{path/to/config}}`

- 通过指定主机和端口连接到 VPN：

`openfortivpn {{host}}:{{port}}`

- 通过传递证书的 sha256 哈希值信任某个网关：

`openfortivpn --trusted-cert={{sha256_sum}}`
