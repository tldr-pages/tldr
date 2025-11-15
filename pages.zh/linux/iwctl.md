# iwctl

> 控制 `iwd` 网络请求程序。
> 更多信息：<https://manned.org/iwctl>.

- 启动交互模式，在此模式您可以直接输入命令并带有自动补全：

`iwctl`

- 显示您的 Wi-Fi 站点：

`iwctl station list`

- 开始寻找带有站点的网络：

`iwctl station {{站点}} scan`

- 显示站点发现的网络：

`iwctl station {{站点}} get-networks`

- 连接到带有站点的网络，如果需要凭证，则会询问：

`iwctl station {{站点}} connect {{网络名称}}`

- 显示帮助：

`iwctl {{[-h|--help]}}`
