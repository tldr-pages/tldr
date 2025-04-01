# if

> 在 shell 脚本中执行条件处理。
> 请参阅：`test`，`[`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>。

- 如果条件命令的退出状态为零，则执行指定的命令：

`if {{condition_command}}; then {{echo "条件为真"}}; fi`

- 如果条件命令的退出状态不为零，则执行指定的命令：

`if ! {{condition_command}}; then {{echo "条件为真"}}; fi`

- 如果条件命令的退出状态为零，则执行第一个指定的命令；否则执行第二个指定的命令：

`if {{condition_command}}; then {{echo "条件为真"}}; else {{echo "条件为假"}}; fi`

- 检查文件是否存在：

`if [[ -f {{path/to/file}} ]]; then {{echo "条件为真"}}; fi`

- 检查目录是否存在：

`if [[ -d {{path/to/directory}} ]]; then {{echo "条件为真"}}; fi`

- 检查文件或目录是否存在：

`if [[ -e {{path/to/file_or_directory}} ]]; then {{echo "条件为真"}}; fi`

- 检查变量是否已定义：

`if [[ -n "${{variable}}" ]]; then {{echo "条件为真"}}; fi`

- 列出所有可能的条件（`test` 是 `[` 的别名；两者通常与 `if` 一起使用）：

`man test`