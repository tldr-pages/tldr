# pdfposter

> 将大幅面 PDF 转换为多个 A4 页面以便打印。
> 更多信息：<https://pdfposter.readthedocs.io>。

- 将 A2 幅面的海报转换为 4 个 A4 页面：

`pdfposter --poster-size a2 {{input_file.pdf}} {{output_file.pdf}}`

- 将 A4 幅面的海报放大到 A3 幅面，然后生成 2 个 A4 页面：

`pdfposter --scale 2 {{input_file.pdf}} {{output_file.pdf}}`