# brew

> Linux 和 macOS 的包管理器。
> 更多信息：<https://brew.sh>.

- 安装最新稳定版的配方（formula）或木桶（cask），使用 `--devel` 安装开发版：

`brew install {{配方}}`

- 列出所有已安装的配方和木桶：

`brew list`

- 升级已安装的配方或木桶（如果没有指定，则升级所有已安装的配方/木桶）：

`brew upgrade {{配方}}`

- 从 Homebrew 源存储库中获取最新版本的 Homebrew 以及所有配方和木桶：

`brew update`

- 显示有新版本的配方和木桶：

`brew outdated`

- 搜索可用的配方（即包）和木桶（即原生包）：

`brew search {{包名}}`

- 显示有关配方或木桶的信息（版本、安装路径、依赖等）：

`brew info {{配方}}`

- 检查本地 Homebrew 安装包是否有潜在问题：

`brew doctor`
