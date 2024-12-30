# echo

> 打印给定的参数。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>。

- 打印一条文本消息。注意：引号是可选的：

`echo "{{你好，世界}}"`

- 打印包含环境变量的消息：

`echo "{{我的路径是 $PATH}}"`

- 打印一条没有换行符的消息：

`echo -n "{{你好，世界}}"`

- 将消息附加到文件中：

`echo "{{你好，世界}}" >> {{file.txt}}`

- 启用对反斜杠转义字符（特殊字符）的解释：

`echo -e "{{列 1\t列 2}}"`

- 打印最后执行命令的退出状态（注意：在Windows命令提示符和PowerShell中，等效命令为`echo %errorlevel%`和`$lastexitcode`）：

`echo $?`