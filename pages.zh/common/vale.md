# vale

> 可扩展的风格检查工具，支持多种标记格式，如 Markdown 和 AsciiDoc。
> 更多信息：<https://vale.sh>。

- 检查文件的风格：

`vale {{path/to/file}}`

- 使用指定的配置检查文件的风格：

`vale --config='{{path/to/.vale.ini}}' {{path/to/file}}`

- 以 JSON 格式输出检查结果：

`vale --output=JSON {{path/to/file}}`

- 检查特定严重程度及其以上的风格问题：

`vale --minAlertLevel={{suggestion|warning|error}} {{path/to/file}}`

- 从 `stdin` 检查风格，指定标记格式：

`cat {{file.md}} | vale --ext=.md`

- 列出当前的配置：

`vale ls-config`