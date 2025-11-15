# brew bundle

> Homebrew，Homebrew Cask 和 Mac App Store的打包器。
> 更多信息：<https://docs.brew.sh/Manpage#bundle-subcommand>.

- 从当前路径下的 Brewfile 安装软件包：

`brew bundle`

- 从特定路径下的特定 Brewfile 安装软件包：

`brew bundle --file {{路径/到/文件}}`

- 基于所有安装的软件包，创建 Brewfile：

`brew bundle dump`

- 卸载所有 Brewfile 中未列出的软件包：

`brew bundle cleanup --force`

- 检查 Brewfile 中指定的包，是否需要安装或升级：

`brew bundle check`

- 列出 Brewfile 中的所有安装包条目：

`brew bundle list --all`
