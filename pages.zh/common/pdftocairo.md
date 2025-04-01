# pdftocairo

> 使用 cairo 将 PDF 文件转换为 PNG/JPEG/TIFF/PDF/PS/EPS/SVG。
> 更多信息：<https://poppler.freedesktop.org>。

- 将 PDF 文件转换为 JPEG：

`pdftocairo {{path/to/file.pdf}} -jpeg`

- 将 PDF 文件转换为 PDF，并扩展输出以填满纸张：

`pdftocairo {{path/to/file.pdf}} {{output.pdf}} -pdf -expand`

- 将 PDF 文件转换为 SVG，并指定要转换的起始页和结束页：

`pdftocairo {{path/to/file.pdf}} {{output.svg}} -svg -f {{first_page}} -l {{last_page}}`

- 将 PDF 文件转换为 200ppi 分辨率的 PNG：

`pdftocairo {{path/to/file.pdf}} {{output.png}} -png -r 200`

- 将 PDF 文件转换为灰度 TIFF，并设置纸张大小为 A3：

`pdftocairo {{path/to/file.pdf}} -tiff -gray -paper A3`

- 将 PDF 文件转换为 PNG，并从左上角裁剪指定的 x 和 y 像素：

`pdftocairo {{path/to/file.pdf}} -png -x {{x_pixels}} -y {{y_pixels}}`