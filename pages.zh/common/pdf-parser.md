# pdf-parser

> 识别 PDF 文件的基本元素，而无需渲染文件。
> 更多信息：<https://blog.didierstevens.com/programs/pdf-tools>.

- 显示 PDF 文件的统计信息：

`pdf-parser --stats {{path/to/file.pdf}}`

- 显示 PDF 文件中类型为 `/Font` 的对象：

`pdf-parser --type={{/Font}} {{path/to/file.pdf}}`

- 在间接对象中搜索字符串：

`pdf-parser --search={{search_string}} {{path/to/file.pdf}}`