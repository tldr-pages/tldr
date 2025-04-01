# protonvpn connect

> 连接到 ProtonVPN。
> 更多信息：<https://github.com/Rafficer/linux-cli-community>.

- 以交互方式连接到 ProtonVPN：

`protonvpn {{[c|connect]}}`

- 使用最快的服务器连接到 ProtonVPN：

`protonvpn {{[c|connect]}} {{[-f|--fastest]}}`

- 使用特定的服务器和特定的协议连接到 ProtonVPN：

`protonvpn {{[c|connect]}} {{server_name}} -p {{udp|tcp}}`

- 使用特定协议的随机服务器连接到 ProtonVPN：

`protonvpn {{[c|connect]}} {{[-r|--random]}} -p {{udp|tcp}}`

- 使用最快的支持 Tor 的服务器连接到 ProtonVPN：

`protonvpn {{[c|connect]}} --tor`

- 显示帮助：

`protonvpn connect --help`