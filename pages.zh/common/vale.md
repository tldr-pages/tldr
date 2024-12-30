# vale

> 可扩展的样式检查器，支持多种标记格式，如Markdown和AsciiDoc。
> 更多信息：<https://vale.sh>。

- 检查文件的样式：

`vale {{path/to/file}}`

- 使用指定配置检查文件的样式：

`vale --config='{{path/to/.vale.ini}}' {{path/to/file}}`

- 以JSON格式输出结果：

`vale --output=JSON {{path/to/file}}`

- 检查特定严重性及更高的样式问题：

`vale --minAlertLevel={{suggestion|warning|error}} {{path/to/file}}`

- 从`stdin`检查样式，指定标记格式：

`cat {{file.md}} | vale --ext=.md`

- 列出当前配置：

`vale ls-config`