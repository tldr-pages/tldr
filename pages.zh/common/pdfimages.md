# pdfimages

> 从PDF中提取图像的工具。
> 更多信息：<https://manned.org/pdfimages>。

- 从PDF文件中提取所有图像并将它们保存为PNG格式：

`pdfimages -png {{path/to/file.pdf}} {{filename_prefix}}`

- 从第3页到第5页提取图像：

`pdfimages -f {{3}} -l {{5}} {{path/to/file.pdf}} {{filename_prefix}}`

- 从PDF文件中提取图像，并在输出文件名中包含页码：

`pdfimages -p {{path/to/file.pdf}} {{filename_prefix}}`

- 列出PDF文件中所有图像的信息：

`pdfimages -list {{path/to/file.pdf}}`