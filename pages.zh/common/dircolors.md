# dircolors

> 输出设置 LS_COLOR 环境变量的命令以自定义 `ls`, `dir` 等的颜色。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- 输出使用默认颜色设置 LS_COLOR 的命令：

`dircolors`

- 显示每个文件类型在 `ls` 中显示的颜色：

`dircolors --print-ls-colors`

- 输出使用来自文件的颜色设置 LS_COLOR 的命令：

`dircolors {{path/to/file}}`

- 输出适用于 Bourne shell 的命令：

`dircolors {{[-b|--bourne-shell]}}`

- 输出适用于 C shell 的命令：

`dircolors {{[-c|--c-shell]}}`

- 查看文件类型和扩展名的默认颜色：

`dircolors {{[-p|--print-database]}}`
