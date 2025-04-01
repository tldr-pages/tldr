# pdfdetach

> 列出或提取 PDF 文件中的附件（嵌入文件）。
> 参见：`pdfattach`, `pdfimages`, `pdfinfo`。
> 更多信息：<https://manned.org/pdfdetach>。

- 列出文件中所有使用特定文本编码的附件：

`pdfdetach list -enc {{UTF-8}} {{path/to/input.pdf}}`

- 通过指定编号保存特定的嵌入文件：

`pdfdetach -save {{number}} {{path/to/input.pdf}}`

- 通过指定名称保存特定的嵌入文件：

`pdfdetach -savefile {{name}} {{path/to/input.pdf}}`

- 将嵌入文件保存为自定义输出文件名：

`pdfdetach -save {{number}} -o {{path/to/output}} {{path/to/input.pdf}}`

- 从受所有者/用户密码保护的文件中保存附件：

`pdfdetach -save {{number}} {{-opw|-upw}} {{password}} {{path/to/input.pdf}}`
