# pdfdetach

> 从 PDF 文件中列出或提取附件（嵌入文件）。
> 另见：`pdfattach`、`pdfimages`、`pdfinfo`。
> 更多信息：<https://manned.org/pdfdetach>。

- 列出文件中所有附件，并指定特定的文本编码：

`pdfdetach list -enc {{UTF-8}} {{path/to/input.pdf}}`

- 通过指定其编号保存特定的嵌入文件：

`pdfdetach -save {{number}} {{path/to/input.pdf}}`

- 通过指定其名称保存特定的嵌入文件：

`pdfdetach -savefile {{name}} {{path/to/input.pdf}}`

- 使用自定义输出文件名保存嵌入文件：

`pdfdetach -save {{number}} -o {{path/to/output}} {{path/to/input.pdf}}`

- 从由所有者/用户密码保护的文件中保存附件：

`pdfdetach -save {{number}} {{-opw|-upw}} {{password}} {{path/to/input.pdf}}`