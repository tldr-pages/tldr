# brew install

> 安装 Homebrew 公式或 Cask。
> 更多信息：<https://docs.brew.sh/Manpage#install-options-formulacask->.

- 安装公式或 Cask：

`brew install {{formula|cask}}`

- 从源代码构建并安装公式（依赖项仍会从瓶中安装）：

`brew install --build-from-source {{formula}}`

- 下载清单，打印将要安装的内容但不实际安装：

`brew install --dry-run {{formula|cask}}`