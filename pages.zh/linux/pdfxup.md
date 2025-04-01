# pdfxup

> N-上 PDF 页面。
> N-上是指通过缩放和旋转将多个页面排列成网格并合并到一个页面上。
> 更多信息：<https://ctan.org/pkg/pdfxup>。

- 创建一个 2-上 PDF：

`pdfxup -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- 创建每页 3 列 2 行的 PDF：

`pdfxup -x {{3}} -y {{2}} -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- 创建小册子模式的 PDF（2-上，页面排序以折叠成书）：

`pdfxup -b -o {{path/to/output.pdf}} {{path/to/input.pdf}}`
