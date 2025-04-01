# iwctl

> 控制 `iwd` 网络管理工具。
> 更多信息：<https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/gettingstarted.html>。

- 启动交互模式，在此模式下，您可以直接输入命令，并带有自动完成功能：

`iwctl`

- 调用通用帮助：

`iwctl --help`

- 显示您的 Wi-Fi 站点：

`iwctl station list`

- 使用站点开始搜索网络：

`iwctl station {{station}} scan`

- 显示站点发现的网络：

`iwctl station {{station}} get-networks`

- 使用站点连接到网络，如果需要凭据，将提示输入：

`iwctl station {{station}} connect {{network_name}}`
