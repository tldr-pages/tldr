# goenv

> 安装、卸载或切换 Golang 版本。
> 支持类似 "1.16.15" 或 "1.22.8" 的版本号。
> 更多信息：<https://github.com/go-nv/goenv>。

- 列出所有可用的 goenv 命令：

`goenv commands`

- 安装特定版本的 Golang：

`goenv install {{go_version}}`

- 在当前项目中使用特定版本的 Golang：

`goenv local {{go_version}}`

- 设置默认的 Golang 版本：

`goenv global {{go_version}}`

- 列出所有可用的 Golang 版本，并高亮显示默认版本：

`goenv versions`

- 卸载指定的 Go 版本：

`goenv uninstall {{go_version}}`

- 使用选定的 Go 版本运行可执行文件：

`goenv exec go run {{go_version}}`
