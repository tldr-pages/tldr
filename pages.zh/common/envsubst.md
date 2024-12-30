# envsubst

> 用它们在 shell 格式字符串中的值替换环境变量。
> 要被替换的变量应以 `${var}` 或 `$var` 格式表示。
> 更多信息：<https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>。

- 在 `stdin` 中替换环境变量并输出到 `stdout`：

`echo '{{$HOME}}' | envsubst`

- 在输入文件中替换环境变量并输出到 `stdout`：

`envsubst < {{path/to/input_file}}`

- 在输入文件中替换环境变量并输出到文件：

`envsubst < {{path/to/input_file}} > {{path/to/output_file}}`

- 从空格分隔的列表中替换输入文件中的环境变量：

`envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}`