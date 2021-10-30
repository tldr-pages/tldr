# brew cask

> macOS 上的应用程序包管理工具。
> 更多信息：<https://github.com/Homebrew/homebrew-cask>.

- 模糊搜索可用命令行工具和软件包：

`brew search {{软件名}}`

- 安装一个软件：

`brew cask install {{软件名}}`

- 列出全部已安装软件：

`brew cask list`

- 列出全部已安装的软件中，可以升级的：

`brew cask outdated`

- 将一个已安装的软件升级到最新的版本：

`brew cask upgrade {{软件名}}`

- 删除一个软件（仅通过 brew cask install 方式安装的）：

`brew cask uninstall {{软件名}}`

- 卸载一个软件并删除相关的设置和文件：

`brew cask zap {{软件名}}`

- 显示指定软件的相关信息：

`brew cask info {{软件名}}`
