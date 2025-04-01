# gox

> 用于跨平台编译 Go 程序。
> 更多信息：<https://github.com/mitchellh/gox>.

- 编译当前目录中的 Go 程序，适用于所有操作系统和架构组合：

`gox`

- 从远程 URL 下载并编译 Go 程序：

`gox {{url_1}} {{url_2}}`

- 为特定操作系统编译当前目录：

`gox -os="{{os}}"`

- 为单个操作系统和架构组合编译当前目录：

`gox -osarch="{{os}}/{{arch}}"`