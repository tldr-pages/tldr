# apt-mark

> 用于更改已安装软件包状态的工具。
> 更多信息：<https://manned.org/apt-mark.8>。

- 将软件包标记为自动安装：

`sudo apt-mark auto {{package}}`

- 将软件包保持在当前版本，防止其更新：

`sudo apt-mark hold {{package}}`

- 允许软件包再次更新：

`sudo apt-mark unhold {{package}}`

- 显示手动安装的软件包：

`apt-mark showmanual`

- 显示未更新的被保持的软件包：

`apt-mark showhold`