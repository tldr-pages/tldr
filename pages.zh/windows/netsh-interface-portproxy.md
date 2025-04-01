# netsh interface portproxy

> 配置和显示各种网络组件的状态。
> 更多信息：<https://learn.microsoft.com/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- 显示当前的端口转发设置：

`netsh interface portproxy show all`

- 设置 IPv4 端口转发（在提升的控制台中运行）：

`netsh interface portproxy add v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}  connectaddress={{10.0.0.1}} connectport={{80}}`

- 删除 IPv4 端口转发（在提升的控制台中运行）：

`netsh interface portproxy delete v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}`

- 显示帮助：

`netsh interface portproxy`