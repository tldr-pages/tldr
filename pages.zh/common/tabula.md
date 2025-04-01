# tabula

> 从 PDF 文件中提取表格。
> 更多信息：<https://tabula.technology>.

- 从 PDF 文件中提取所有表格到 CSV 文件：

`tabula -o {{file.csv}} {{file.pdf}}`

- 从 PDF 文件中提取所有表格到 JSON 文件：

`tabula --format JSON -o {{file.json}} {{file.pdf}}`

- 从 PDF 文件的第 1、2、3 和 6 页提取表格：

`tabula --pages {{1-3,6}} {{file.pdf}}`

- 从 PDF 文件的第 1 页提取表格，并猜测要检查的页面部分：

`tabula --guess --pages {{1}} {{file.pdf}}`

- 从 PDF 文件中提取所有表格，使用规则线确定单元格边界：

`tabula --spreadsheet {{file.pdf}}`

- 从 PDF 文件中提取所有表格，使用空白区域确定单元格边界：

`tabula --no-spreadsheet {{file.pdf}}`