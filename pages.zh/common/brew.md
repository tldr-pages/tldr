# brew

> Homebrew - macOS和Linux的包管理器。
> 一些子命令如`install`有自己的使用文档。
> 更多信息：<https://docs.brew.sh/Manpage>。

- 安装公式或cask的最新稳定版本（使用`--devel`安装开发版本）：

`brew install {{formula}}`

- 列出所有已安装的公式和cask：

`brew list`

- 升级已安装的公式或cask（如果未指定，则升级所有已安装的公式/cask）：

`brew upgrade {{formula}}`

- 从Homebrew源代码库获取Homebrew及所有公式和cask的最新版本：

`brew update`

- 显示有更高版本可用的公式和cask：

`brew outdated`

- 搜索可用的公式（即包）和cask（即本地macOS `.app`包）：

`brew search {{text}}`

- 显示有关公式或cask的信息（版本、安装路径、依赖项等）：

`brew info {{formula}}`

- 检查本地Homebrew安装的潜在问题：

`brew doctor`