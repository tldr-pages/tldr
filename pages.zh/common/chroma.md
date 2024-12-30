# chroma

> 一个通用的语法高亮工具。
> `--lexer` 选项通常是不必要的，因为它会根据文件扩展名自动确定。
> 更多信息：<https://github.com/alecthomas/chroma>。

- 使用 Python 词法分析器高亮显示文件中的源代码并输出到 `stdout`：

`chroma --lexer {{python}} {{path/to/source_file.py}}`

- 使用 Go 词法分析器高亮显示文件中的源代码并输出到 HTML 文件：

`chroma --lexer {{go}} --formatter {{html}} {{path/to/source_file.go}} > {{path/to/target_file.html}}`

- 使用 C++ 词法分析器从 `stdin` 中高亮显示源代码并输出到 SVG 文件，使用 Monokai 风格：

`{{command}} | chroma --lexer {{c++}} --formatter {{svg}} --style {{monokai}} > {{path/to/target_file.svg}}`

- 列出可用的词法分析器、风格和格式化器：

`chroma --list`