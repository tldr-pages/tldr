# dircolors

> 输出命令以设置 LS_COLOR 环境变量并为 `ls`、`dir` 等命令设置样式。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>。

- 使用默认颜色输出设置 LS_COLOR 的命令：

`dircolors`

- 显示每种文件类型在 `ls` 中的显示颜色：

`dircolors --print-ls-colors`

- 使用文件中的颜色输出设置 LS_COLOR 的命令：

`dircolors {{path/to/file}}`

- 输出 Bourne shell 的命令：

`dircolors --bourne-shell`

- 输出 C shell 的命令：

`dircolors --c-shell`

- 查看文件类型和扩展名的默认颜色：

`dircolors --print-data`