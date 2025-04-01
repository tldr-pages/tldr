# ksh

> Korn Shell，一个兼容 Bash 的命令行解释器。
> 参见：`!`，`^`。
> 更多信息：<https://manned.org/ksh>。

- 启动一个交互式的 shell 会话：

`ksh`

- 执行特定的 [c]ommands：

`ksh -c "{{echo 'ksh is executed'}}"`

- 执行特定的脚本：

`ksh {{path/to/script.ksh}}`

- 检查特定脚本的语法错误而不执行它：

`ksh -n {{path/to/script.ksh}}`

- 执行特定的脚本，打印脚本中的每个命令然后再执行它：

`ksh -x {{path/to/script.ksh}}`
