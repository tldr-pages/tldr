# brew 安装

> 安装一个 Homebrew 配方或 Cask。
> 更多信息: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- 安装一个配方/Cask:

`brew install {{配方|Cask}}`

- 从源代码构建并安装一个配方（依赖项仍将从瓶子中安装）:

`brew install --build-from-source {{配方}}`

- 下载清单，打印将要安装的内容，但实际上不安装任何东西:

`brew install --dry-run {{配方|Cask}}`