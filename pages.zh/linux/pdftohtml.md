# pdftohtml

> 将 PDF 文件转换为 HTML、XML 和 PNG 图像。
> 更多信息：<https://manned.org/pdftohtml>.

- 将 PDF 文件转换为 HTML 文件：

`pdftohtml {{path/to/file.pdf}} {{path/to/output_file.html}}`

- 忽略 PDF 文件中的图像：

`pdftohtml -i {{path/to/file.pdf}} {{path/to/output_file.html}}`

- 生成一个包含所有 PDF 页的单一 HTML 文件：

`pdftohtml -s {{path/to/file.pdf}} {{path/to/output_file.html}}`

- 将 PDF 文件转换为 XML 文件：

`pdftohtml -xml {{path/to/file.pdf}} {{path/to/output_file.xml}}`
