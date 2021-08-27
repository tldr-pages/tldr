# brew

> Linux 的 Homebrew 包管理器。
> 更多信息：<https://docs.brew.sh/Homebrew-on-Linux>.

- 搜索可用的软件包：

`brew search {{包名}}`

- 安装最新版的包（使用 --devel 获取开发版）：

`brew install {{包名}}`

- 列出所有已安装的包：

`brew list`

- 更新已安装的包（如果未指定，则更新所有包）：

`brew upgrade {{包名}}`

- 从 GitHub 更新到最新版本的 Linuxbrew 和所有包：

`brew update`

- 显示有更新版本可用的包：

`brew outdated`

- 显示一个包的信息（版本、安装路径、依赖等）：

`brew info {{包名}}`

- 检查本地 Linuxbrew 安装是否存在潜在问题：

`brew doctor`
