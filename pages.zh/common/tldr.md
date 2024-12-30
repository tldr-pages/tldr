# tldr

> 显示来自 tldr-pages 项目的命令行工具简单帮助页面。
> 注意：`--language` 和 `--list` 选项并不是客户端规范所要求的，但大多数客户端实现了它们。
> 更多信息：<https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>。

- 打印特定命令的 tldr 页面（提示：这就是你来到这里的方式！）：

`tldr {{command}}`

- 打印特定子命令的 tldr 页面：

`tldr {{command}} {{subcommand}}`

- 打印给定 [L]anguage 中命令的 tldr 页面（如果可用，否则回退到英语）：

`tldr --language {{language_code}} {{command}}`

- 打印来自特定 [p]latform 的命令的 tldr 页面：

`tldr --platform {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{command}}`

- [u]pdate 本地 tldr 页面缓存：

`tldr --update`

- [l]ist 当前平台和 `common` 的所有页面：

`tldr --list`

- [l]ist 特定命令的所有可用子命令页面：

`tldr --list | grep {{command}} | column`