# pdftocairo

> 使用cairo将PDF文件转换为PNG/JPEG/TIFF/PDF/PS/EPS/SVG。
> 更多信息：<https://poppler.freedesktop.org>。

- 将PDF文件转换为JPEG：

`pdftocairo {{path/to/file.pdf}} -jpeg`

- 转换为PDF并将输出扩展以填充纸张：

`pdftocairo {{path/to/file.pdf}} {{output.pdf}} -pdf -expand`

- 转换为SVG，指定要转换的第一页/最后一页：

`pdftocairo {{path/to/file.pdf}} {{output.svg}} -svg -f {{first_page}} -l {{last_page}}`

- 以200ppi分辨率转换为PNG：

`pdftocairo {{path/to/file.pdf}} {{output.png}} -png -r 200`

- 转换为灰度TIFF并将纸张大小设置为A3：

`pdftocairo {{path/to/file.pdf}} -tiff -gray -paper A3`

- 转换为PNG，从左上角剪裁x和y像素：

`pdftocairo {{path/to/file.pdf}} -png -x {{x_pixels}} -y {{y_pixels}}`