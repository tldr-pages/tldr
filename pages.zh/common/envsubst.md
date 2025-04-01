# envsubst

> 替换 shell 格式字符串中的环境变量。
> 要替换的变量应为 `${var}` 或 `$var` 格式。
> 更多信息：<https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- 替换 `stdin` 中的环境变量，并输出到 `stdout`：

`echo '{{$HOME}}' | envsubst`

- 替换输入文件中的环境变量，并输出到 `stdout`：

`envsubst < {{path/to/input_file}}`

- 替换输入文件中的环境变量，并输出到文件：

`envsubst < {{path/to/input_file}} > {{path/to/output_file}}`

- 从空格分隔的列表中替换输入文件中的环境变量：

`envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}`