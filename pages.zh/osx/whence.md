# whence

> Zsh 内置命令，用于指示命令将如何被解释。
> 更多信息：<https://keith.github.io/xcode-man-pages/whence.1.html>.

- 解释 `command`，如果定义为 `alias` 则进行扩展（类似于 `command -v` 内置命令）：

`whence "{{command}}"`

- 显示 `command` 的类型，如果定义为函数或二进制文件，则显示其位置（相当于 `type` 和 `command -V` 内置命令）：

`whence -v "{{command}}"`

- 与上述相同，但显示 shell 函数的内容而不是位置（相当于 `which` 内置命令）：

`whence -c "{{command}}"`

- 与上述相同，但显示命令路径上的所有出现位置（相当于 `where` 内置命令）：

`whence -ca "{{command}}"`

- 仅在 `PATH` 中搜索 `command`，忽略内置命令、别名或 shell 函数（相当于 `where` 命令）：

`whence -p "{{command}}"`
