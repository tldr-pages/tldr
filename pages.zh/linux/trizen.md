# trizen

> Arch Linux 的工具，用于从 Arch 用户仓库 (AUR) 构建软件包。
> 更多信息：<https://github.com/trizen/trizen>。

- 同步并更新所有 AUR 软件包：

`trizen -Syua`

- 安装新软件包：

`trizen -S {{package}}`

- 卸载软件包及其依赖项：

`trizen -Rs {{package}}`

- 在软件包数据库中搜索关键词：

`trizen -Ss {{keyword}}`

- 显示关于软件包的信息：

`trizen -Si {{package}}`

- 列出已安装的软件包及其版本：

`trizen -Qe`