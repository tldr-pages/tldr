# brew bundle

> Homebrew、Homebrew Cask 和 Mac App Store 的打包工具。
> 更多信息：<https://github.com/Homebrew/homebrew-bundle>。

- 从当前路径的 Brewfile 安装软件包：

`brew bundle`

- 从特定路径的特定 Brewfile 安装软件包：

`brew bundle --file {{path/to/file}}`

- 从所有已安装的软件包创建一个 Brewfile：

`brew bundle dump`

- 卸载所有未列在 Brewfile 中的公式：

`brew bundle cleanup --force`

- 检查 Brewfile 中是否有需要安装或升级的内容：

`brew bundle check`

- 列出 Brewfile 中的所有条目：

`brew bundle list --all`