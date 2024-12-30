# wkhtmltopdf

> 一个开源命令行工具，用于将HTML文档或网页转换为PDF文件。
> 更多信息：<https://wkhtmltopdf.org/>.

- 将HTML文档转换为PDF：

`wkhtmltopdf {{input.html}} {{output.pdf}}`

- 指定PDF页面大小（请参见`QPrinter`的`PaperSize`以获取支持的大小）：

`wkhtmltopdf --page-size {{A4}} {{input.html}} {{output.pdf}}`

- 设置PDF页面边距：

`wkhtmltopdf --margin-{{top|bottom|left|right}} {{10mm}} {{input.html}} {{output.pdf}}`

- 设置PDF页面方向：

`wkhtmltopdf --orientation {{Landscape|Portrait}} {{input.html}} {{output.pdf}}`

- 生成PDF文档的灰度版本：

`wkhtmltopdf --grayscale {{input.html}} {{output.pdf}}`