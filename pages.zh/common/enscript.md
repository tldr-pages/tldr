# enscript

> 将文本文件转换为 PostScript、HTML、RTF、ANSI 和压印等格式。
> 更多信息：<https://manned.org/enscript>.

- 从文本文件生成一个 PostScript 文件：

`enscript {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- 生成非 PostScript 格式的文件：

`enscript {{path/to/input_file}} {{[-w|--language]}} {{html|rtf|...}} {{[-o|--output]}} {{path/to/output_file}}`

- 生成一个包含横向布局的 PostScript 文件，并将页面分成列（最多 9 列）：

`enscript {{path/to/input_file}} --columns {{num}} {{[-r|--landscape]}} {{[-o|--output]}} {{path/to/output_file}}`

- 显示可用的语法高亮语言和文件格式：

`enscript --help-highlight`

- 生成一个带有指定语言语法高亮和颜色的 PostScript 文件：

`enscript {{path/to/input_file}} --color 1 {{[-E|--highlight]}} {{language}} {{[-o|--output]}} {{path/to/output_file}}`