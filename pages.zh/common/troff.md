# troff

> 用于 groff (GNU Troff) 文档格式系统的排版处理器。
> 另见 `groff`。
> 更多信息：<https://manned.org/troff>。

- 为 PostScript 打印机格式化输出，并将输出保存到文件：

`troff {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- 使用 [me] 宏包为 PostScript 打印机格式化输出，并将输出保存到文件：

`troff -{{me}} {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- 使用 [man] 宏包将输出格式化为 [a]SCII 文本：

`troff -T {{ascii}} -{{man}} {{path/to/input.roff}} | grotty`

- 将输出格式化为 [pdf] 文件，并将输出保存到文件：

`troff -T {{pdf}} {{path/to/input.roff}} | gropdf > {{path/to/output.pdf}}`