# iwctl

> 控制 `iwd` 网络补助程序。
> 更多信息：<https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/gettingstarted.html>。

- 启动交互模式，在此模式下您可以直接输入命令，并支持自动补全：

`iwctl`

- 调用一般帮助：

`iwctl --help`

- 显示您的 Wi-Fi 站点：

`iwctl station list`

- 开始使用站点搜索网络：

`iwctl station {{station}} scan`

- 显示站点找到的网络：

`iwctl station {{station}} get-networks`

- 使用站点连接到网络，如果需要凭据，会提示输入：

`iwctl station {{station}} connect {{network_name}}`