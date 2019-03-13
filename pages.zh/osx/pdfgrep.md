# pdfgrep

> 在PDF文件中搜索文本.

- 在PDF中查找与关键词匹配的行:

`pdfgrep {{关键词}} {{文件.pdf}}`

- 包含每个匹配行的文件名和页码:

`pdfgrep --with-filename --page-number {{关键词}} {{文件.pdf}}`

- 对以 "foo" 开头关键词搜索,返回前3个匹配项,不区分大小写:

`pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{文件.pdf}}`

- 在当前目录中扩展名为.pdf的文件中递归查找关键词:

`pdfgrep --recursive {{关键词}}`

- 在与当前目录中特定文件名 "*book.pdf" 匹配的文件上递归查找关键词:

`pdfgrep --recursive --include {{'*book.pdf'}} {{关键词}}`
