# goreload

> Go 程序的实时重载工具。
> 更多信息：<https://github.com/acoshift/goreload>。

- 监视二进制文件（默认为 `.goreload`）：

`goreload -b {{path/to/binary}} {{path/to/file.go}}`

- 设置自定义日志前缀（默认为 `goreload`）：

`goreload --logPrefix {{prefix}} {{path/to/file.go}}`

- 无论何时文件发生变化时重载：

`goreload --all`
