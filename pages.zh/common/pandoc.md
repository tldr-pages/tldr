# pandoc

> 在各种格式之间转换文档。
> 更多信息：<https://pandoc.org/MANUAL.html>。

- 将文件转换为PDF（输出格式由文件扩展名决定）：

`pandoc {{path/to/input.md}} {{-o|--output}} {{path/to/output.pdf}}`

- 转换为带有适当页眉/页脚的独立文件（适用于LaTeX、HTML等）：

`pandoc {{path/to/input.md}} {{-s|--standalone}} {{-o|--output}} {{path/to/output.html}}`

- 手动指定格式检测和转换（覆盖使用文件名扩展名的自动格式检测或当文件名扩展名完全缺失时）：

`pandoc {{-f|-r|--from|--read}} {{docx|...}} {{path/to/input}} {{-t|-w|--to|--write}} {{pdf|...}} {{-o|--output}} {{path/to/output}}`

- 列出所有支持的输入格式：

`pandoc --list-input-formats`

- 列出所有支持的输出格式：

`pandoc --list-output-formats`