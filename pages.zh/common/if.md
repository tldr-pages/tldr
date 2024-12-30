# 如果

> 在 shell 脚本中执行条件处理。
> 另见：`test`，`[`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>。

- 如果条件命令的退出状态为零，则执行指定的命令：

`if {{condition_command}}; then {{echo "条件为真"}}; fi`

- 如果条件命令的退出状态不为零，则执行指定的命令：

`if ! {{condition_command}}; then {{echo "条件为真"}}; fi`

- 如果条件命令的退出状态为零，则执行第一组指定的命令，否则执行第二组指定的命令：

`if {{condition_command}}; then {{echo "条件为真"}}; else {{echo "条件为假"}}; fi`

- 检查一个 [f]ile 是否存在：

`if [[ -f {{path/to/file}} ]]; then {{echo "条件为真"}}; fi`

- 检查一个 [d]irectory 是否存在：

`if [[ -d {{path/to/directory}} ]]; then {{echo "条件为真"}}; fi`

- 检查一个文件或目录 [e]xists：

`if [[ -e {{path/to/file_or_directory}} ]]; then {{echo "条件为真"}}; fi`

- 检查一个变量是否已定义：

`if [[ -n "${{variable}}" ]]; then {{echo "条件为真"}}; fi`

- 列出所有可能的条件（`test` 是 `[` 的别名；两者通常与 `if` 一起使用）：

`man [`