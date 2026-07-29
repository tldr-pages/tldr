# shopt

> 管理 Bash shell 选项：控制 Bash 特有行为的变量（存储在 `$BASHOPTS` 中）。
> 通用 POSIX shell 变量（存储在 `$SHELLOPTS` 中）使用 `set` 命令管理。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#The-Shopt-Builtin>。

- 列出所有可设置的选项及其是否已设置：

`shopt`

- 设置选项：

`shopt -s {{选项名}}`

- 取消设置选项：

`shopt -u {{选项名}}`

- 以可运行的 `shopt` 命令格式打印所有选项及其状态列表：

`shopt -p`

- 显示帮助信息：

`help shopt`
