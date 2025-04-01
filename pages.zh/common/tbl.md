# tbl

> groff (GNU Troff) 文档格式系统的表格预处理器。
> 也请参阅 `groff` 和 `troff`。
> 更多信息：<https://manned.org/tbl>。

- 处理包含表格的输入文件，保存输出以供使用 groff 转换为 PostScript：

`tbl {{path/to/input_file}} > {{path/to/output.roff}}`

- 使用 [me] 宏包将包含表格的输入文件转换为 PDF：

`tbl -T {{pdf}} {{path/to/input.tbl}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`