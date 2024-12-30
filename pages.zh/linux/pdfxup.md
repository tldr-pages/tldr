# pdfxup

> N-up PDF页面。
> N-upping意味着通过缩放和旋转将多个页面放置到一页上，形成一个网格。
> 更多信息：<https://ctan.org/pkg/pdfxup>。

- 创建一个2页合一的PDF：

`pdfxup -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- 创建一个每页有3列和2行的PDF：

`pdfxup -x {{3}} -y {{2}} -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- 创建一本小册子模式的PDF（2合一，并且页面在折叠时排序成一本书）：

`pdfxup -b -o {{path/to/output.pdf}} {{path/to/input.pdf}}`