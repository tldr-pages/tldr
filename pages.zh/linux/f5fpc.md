# f5fpc

> 一个由 BIG-IP Edge 提供的专有商业 SSL VPN 客户端。
> 更多信息：<https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>。

- 打开新的 VPN 连接：

`sudo f5fpc --start`

- 打开与特定主机的新 VPN 连接：

`sudo f5fpc --start --host {{host.example.com}}`

- 指定用户名（系统会提示输入密码）：

`sudo f5fpc --start --host {{host.example.com}} --username {{user}}`

- 显示当前 VPN 状态：

`sudo f5fpc --info`

- 关闭 VPN 连接：

`sudo f5fpc --stop`