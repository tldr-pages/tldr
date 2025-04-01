# pdftoppm

> 将 PDF 文档页面转换为便携式像素图（图像格式）。
> 更多信息：<https://manned.org/pdftoppm>。

- 指定要转换的页面范围（`n` - 起始页，`m` - 结束页）：

`pdftoppm -f {{n}} -l {{m}} {{path/to/file.pdf}} {{image_name_prefix}}`

- 仅转换 PDF 的第一页：

`pdftoppm -singlefile {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成单色 PBM 文件（而不是彩色 PPM 文件）：

`pdftoppm -mono {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成灰度 PGM 文件（而不是彩色 PPM 文件）：

`pdftoppm -gray {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成 PNG 文件而不是 PPM 文件：

`pdftoppm -png {{path/to/file.pdf}} {{image_name_prefix}}`