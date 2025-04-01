# wkhtmltopdf

> 一个用于将 HTML 文档或网页转换为 PDF 文件的开源命令行工具。
> 更多信息：<https://wkhtmltopdf.org/>.

- 将 HTML 文档转换为 PDF：

`wkhtmltopdf {{input.html}} {{output.pdf}}`

- 指定 PDF 页面大小（支持的大小请参见 `QPrinter` 的 `PaperSize`）：

`wkhtmltopdf --page-size {{A4}} {{input.html}} {{output.pdf}}`

- 设置 PDF 页面边距：

`wkhtmltopdf --margin-{{top|bottom|left|right}} {{10mm}} {{input.html}} {{output.pdf}}`

- 设置 PDF 页面方向：

`wkhtmltopdf --orientation {{Landscape|Portrait}} {{input.html}} {{output.pdf}}`

- 生成 PDF 文档的灰度版本：

`wkhtmltopdf --grayscale {{input.html}} {{output.pdf}}`