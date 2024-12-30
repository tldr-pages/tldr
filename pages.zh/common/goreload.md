# goreload

> Go 程序的实时重载工具。
> 更多信息：<https://github.com/acoshift/goreload>。

- 监视一个二进制文件（默认使用 `.goreload`）：

`goreload -b {{path/to/binary}} {{path/to/file.go}}`

- 设置自定义日志前缀（默认使用 `goreload`）：

`goreload --logPrefix {{prefix}} {{path/to/file.go}}`

- 每当任何文件更改时重新加载：

`goreload --all`