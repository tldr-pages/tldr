# pdfposter

> 将大幅面PDF转换为多个A4页面以便打印。
> 更多信息：<https://pdfposter.readthedocs.io>。

- 将A2海报转换为4个A4页面：

`pdfposter --poster-size a2 {{input_file.pdf}} {{output_file.pdf}}`

- 将A4海报缩放到A3，然后生成2个A4页面：

`pdfposter --scale 2 {{input_file.pdf}} {{output_file.pdf}}`