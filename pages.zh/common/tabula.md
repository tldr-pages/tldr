# tabula

> 从 PDF 文件中提取表格。
> 更多信息：<https://tabula.technology>。

- 将 PDF 中的所有表格提取到 CSV 文件中：

`tabula -o {{file.csv}} {{file.pdf}}`

- 将 PDF 中的所有表格提取到 JSON 文件中：

`tabula --format JSON -o {{file.json}} {{file.pdf}}`

- 从 PDF 的第 1、2、3 和 6 页提取表格：

`tabula --pages {{1-3,6}} {{file.pdf}}`

- 从 PDF 的第 1 页提取表格，猜测要检查的页面部分：

`tabula --guess --pages {{1}} {{file.pdf}}`

- 从 PDF 中提取所有表格，使用划线确定单元格边界：

`tabula --spreadsheet {{file.pdf}}`

- 从 PDF 中提取所有表格，使用空白空间确定单元格边界：

`tabula --no-spreadsheet {{file.pdf}}`