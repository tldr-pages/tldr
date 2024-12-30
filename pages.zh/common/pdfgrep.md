# pdfgrep

> 在PDF文件中搜索文本。
> 更多信息：<https://pdfgrep.org>。

- 在PDF中查找与模式匹配的行：

`pdfgrep {{pattern}} {{file.pdf}}`

- 为每个匹配的行包含文件名和页码：

`pdfgrep --with-filename --page-number {{pattern}} {{file.pdf}}`

- 对以“foo”开头的行进行不区分大小写的搜索，并返回前3个匹配：

`pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{file.pdf}}`

- 在当前目录中递归查找扩展名为`.pdf`的文件中的模式：

`pdfgrep --recursive {{pattern}}`

- 在当前目录中递归查找与特定通配符匹配的文件中的模式：

`pdfgrep --recursive --include {{'*book.pdf'}} {{pattern}}`