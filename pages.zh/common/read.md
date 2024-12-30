# read

> Shell 内置命令，用于从 `stdin` 中检索数据。
> 更多信息：<https://manned.org/read.1p>。

- 存储您从键盘输入的数据：

`read {{variable}}`

- 将您输入的每一行存储为数组的值：

`read -a {{array}}`

- 指定要读取的最大字符数：

`read -n {{character_count}} {{variable}}`

- 将多个值分配给多个变量：

`read {{_ variable1 _ variable2}} <<< "{{姓氏是邦德}}"`

- 不让反斜杠（\\）充当转义字符：

`read -r {{variable}}`

- 在输入之前显示提示：

`read -p "{{在此输入您的内容: }}" {{variable}}`

- 不回显输入的字符（静默模式）：

`read -s {{variable}}`

- 读取 `stdin` 并对每一行执行一个操作：

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{/dev/stdin|path/to/file|...}}`