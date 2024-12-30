# pdfattach

> 向现有的 PDF 文件添加一个新的附件（嵌入文件）。
> 另见：`pdfdetach`，`pdfimages`，`pdfinfo`。
> 更多信息：<https://manned.org/pdfattach>。

- 向现有的 PDF 文件添加新的附件：

`pdfattach {{path/to/input.pdf}} {{path/to/file_to_attach}} {{path/to/output.pdf}}`

- 如果存在同名的附件，则替换它：

`pdfattach -replace {{path/to/input.pdf}} {{path/to/file_to_attach}} {{path/to/output.pdf}}`

- 显示帮助信息：

`pdfattach -h`

- 显示版本信息：

`pdfattach -v`