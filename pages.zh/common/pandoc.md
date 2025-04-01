# pandoc

> 在各种格式之间转换文档。
> 更多信息：<https://pandoc.org/MANUAL.html>.

- 将文件转换为 PDF（输出格式由文件扩展名决定）：

`pandoc {{path/to/input.md}} {{[-o|--output]}} {{path/to/output.pdf}}`

- 将文件转换为独立文件，并包含适当的头部和尾部（适用于 LaTeX、HTML 等）：

`pandoc {{path/to/input.md}} {{[-s|--standalone]}} {{[-o|--output]}} {{path/to/output.html}}`

- 手动指定输入和输出格式（当文件扩展名缺失或需要覆盖自动格式检测时）：

`pandoc {{-f|-r|--from|--read}} {{docx|...}} {{path/to/input}} {{-t|-w|--to|--write}} {{pdf|...}} {{[-o|--output]}} {{path/to/output}}`

- 列出所有支持的输入格式：

`pandoc --list-input-formats`

- 列出所有支持的输出格式：

`pandoc --list-output-formats`