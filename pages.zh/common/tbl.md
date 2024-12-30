# tbl

> 用于 groff（GNU Troff）文档格式化系统的表格预处理器。
> 另请参见 `groff` 和 `troff`。
> 更多信息：<https://manned.org/tbl>。

- 处理包含表格的输入，并将输出保存以便将来使用 groff 排版为 PostScript：

`tbl {{path/to/input_file}} > {{path/to/output.roff}}`

- 使用 [me] 宏包将包含表格的输入排版为 PDF：

`tbl -T {{pdf}} {{path/to/input.tbl}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`