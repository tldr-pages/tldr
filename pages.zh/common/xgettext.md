# xgettext

> 从代码文件中提取 gettext 字符串。
> 更多信息：<https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html>。

- 扫描文件并将字符串输出到 `messages.po`：

`xgettext {{path/to/input_file}}`

- 使用不同的输出文件名：

`xgettext {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- 将新字符串追加到现有文件中：

`xgettext {{[-j|--join-existing]}} {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- 不在输出文件中添加包含元数据的头部信息：

`xgettext --omit-header {{path/to/input_file}}`

- 显示帮助：

`xgettext {{[-h|--help]}}`