# enscript

> 将文本文件转换为 PostScript、HTML、RTF、ANSI 和叠加文本。
> 更多信息：<https://www.gnu.org/software/enscript>。

- 从文本文件生成 PostScript 文件：

`enscript {{path/to/input_file}} --output={{path/to/output_file}}`

- 生成与 PostScript 不同语言的文件：

`enscript {{path/to/input_file}} --language={{html|rtf|...}} --output={{path/to/output_file}}`

- 生成具有横向布局的 PostScript 文件，将页面分割成列（最多 9 列）：

`enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}`

- 显示可用的语法高亮语言和文件格式：

`enscript --help-highlight`

- 生成带有语法高亮和指定语言颜色的 PostScript 文件：

`enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}`