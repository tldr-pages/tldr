# pdfcrop

> 检测并删除 PDF 文件每页的页边距。
> 更多信息：<https://github.com/ho-tex/pdfcrop>.

- 自动检测并删除 PDF 文件每页的页边距：

`pdfcrop {{path/to/input_file.pdf}} {{path/to/output_file.pdf}}`

- 将每页的页边距设置为特定值：

`pdfcrop {{path/to/input_file.pdf}} --margins '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- 将每页的页边距设置为特定值，使用相同的值为左、上、右和下：

`pdfcrop {{path/to/input_file.pdf}} --margins {{300}} {{path/to/output_file.pdf}}`

- 使用用户定义的边界框裁剪，而不是自动检测：

`pdfcrop {{path/to/input_file.pdf}} --bbox '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- 为奇数页和偶数页使用不同的用户定义边界框：

`pdfcrop {{path/to/input_file.pdf}} --bbox-odd '{{left}} {{top}} {{right}} {{bottom}}' --bbox-even '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- 使用较低的分辨率自动检测页边距以提高性能：

`pdfcrop {{path/to/input_file.pdf}} --resolution {{72}} {{path/to/output_file.pdf}}`