# protonvpn 连接

> 连接到 ProtonVPN。
> 更多信息: <https://github.com/Rafficer/linux-cli-community>。

- 交互式连接到 ProtonVPN：

`protonvpn {{c|connect}}`

- 使用最快的可用服务器连接到 ProtonVPN：

`protonvpn {{c|connect}} {{-f|--fastest}}`

- 使用特定协议连接到特定服务器的 ProtonVPN：

`protonvpn {{c|connect}} {{server_name}} -p {{udp|tcp}}`

- 使用特定协议连接到随机服务器的 ProtonVPN：

`protonvpn {{c|connect}} {{-r|--random}} -p {{udp|tcp}}`

- 使用支持 Tor 的最快服务器连接到 ProtonVPN：

`protonvpn {{c|connect}} --tor`

- 显示帮助：

`protonvpn connect --help`