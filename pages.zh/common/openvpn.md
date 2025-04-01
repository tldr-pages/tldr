# openvpn

> OpenVPN 客户端和守护进程二进制文件。
> 更多信息：<https://openvpn.net/>。

- 使用配置文件连接到服务器：

`sudo openvpn {{path/to/client.conf}}`

- 尝试在 bob.example.com 主机上设置一个不安全的点对点隧道：

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}}`

- 无加密连接到等待中的 bob.example.com 主机：

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}}`

- 创建一个加密密钥并保存到文件：

`openvpn --genkey secret {{path/to/key}}`

- 尝试在 bob.example.com 主机上使用静态密钥设置点对点隧道：

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}} --secret {{path/to/key}}`

- 使用与 bob.example.com 相同的静态密钥连接到等待中的 bob.example.com 主机：

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}} --secret {{path/to/key}}`
