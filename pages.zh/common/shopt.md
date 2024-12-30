# shopt

> 管理 Bash shell 选项：存储在 `$BASHOPTS` 中的变量，控制特定于 Bash shell 的行为。
> 通用 POSIX shell 变量（存储在 `$SHELLOPTS` 中）则使用 `set` 命令来管理。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>。

- 所有可设置选项的列表及其设置状态：

`shopt`

- 设置一个选项：

`shopt -s {{option_name}}`

- 取消设置一个选项：

`shopt -u {{option_name}}`

- 打印所有选项及其状态的列表，以可运行的 `shopt` 命令格式显示：

`shopt -p`

- 显示帮助信息：

`help shopt`