# ksh

> Korn Shell，一个与 Bash 兼容的命令行解释器。
> 另见：`histexpand`。
> 更多信息：<http://kornshell.com>。

- 启动一个交互式 shell 会话：

`ksh`

- 执行特定的 [c]ommands：

`ksh -c "{{echo 'ksh 被执行'}}"`

- 执行特定脚本：

`ksh {{path/to/script.ksh}}`

- 检查特定脚本的语法错误而不执行它：

`ksh -n {{path/to/script.ksh}}`

- 执行特定脚本，在执行每个命令之前打印该命令：

`ksh -x {{path/to/script.ksh}}`