# tldr

> 显示来自 tldr-pages 项目的命令行工具的简单帮助页面。
> 注意：`--language` 和 `--list` 选项并非客户端规范所必需，但大多数客户端都实现了它们。
> 更多信息：<https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- 打印指定命令的 tldr 页面（提示：这就是你来到这里的方式！）：

`tldr {{命令}}`

- 打印指定子命令的 tldr 页面：

`tldr {{命令}} {{子命令}}`

- 用指定语言打印命令的 tldr 页面（如果没有，返回英语）：

`tldr {{[-L|--language]}} {{语言代码}} {{命令}}`

- 打印指定平台的命令的 tldr 页面：

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{命令}}`

- 更新 tldr 页面的本地缓存：

`tldr {{[-u|--update]}}`

- 列出当前平台和 `common` 的所有页面：

`tldr {{[-l|--list]}}`

- 列出某个命令的所有可用子命令页面：

`tldr {{[-l|--list]}} | grep {{命令}} | column`

- 打印随机命令的 tldr 页面：

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
