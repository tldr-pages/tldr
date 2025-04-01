# pdfimages

> 用于从 PDF 文件中提取图像的工具。
> 更多信息：<https://manned.org/pdfimages>.

- 从 PDF 文件中提取所有图像并保存为 PNG 格式：

`pdfimages -png {{path/to/file.pdf}} {{filename_prefix}}`

- 从第 3 页到第 5 页提取图像：

`pdfimages -f {{3}} -l {{5}} {{path/to/file.pdf}} {{filename_prefix}}`

- 从 PDF 文件中提取图像并在输出文件名中包含页码：

`pdfimages -p {{path/to/file.pdf}} {{filename_prefix}}`

- 列出 PDF 文件中所有图像的信息：

`pdfimages -list {{path/to/file.pdf}}`