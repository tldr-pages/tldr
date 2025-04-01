# shopt

> 管理 Bash shell 选项：这些变量（存储在 `$BASHOPTS`）控制特定于 Bash shell 的行为。
> 通用的 POSIX shell 变量（存储在 `$SHELLOPTS`）则通过 `set` 命令进行管理。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>.

- 列出所有可设置的选项及其状态：

`shopt`

- 设置一个选项：

`shopt -s {{option_name}}`

- 取消设置一个选项：

`shopt -u {{option_name}}`

- 以可运行的 `shopt` 命令格式列出所有选项及其状态：

`shopt -p`

- 显示帮助：

`help shopt`
