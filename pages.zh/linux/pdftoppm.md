# pdftoppm

> 将PDF文档页面转换为可移植的Pixmap（图像格式）。
> 更多信息：<https://manned.org/pdftoppm>。

- 指定要转换的页面范围（N-第一页面，M-最后一页面）：

`pdftoppm -f {{N}} -l {{M}} {{path/to/file.pdf}} {{image_name_prefix}}`

- 仅转换PDF的第一页：

`pdftoppm -singlefile {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成单色PBM文件（而不是彩色PPM文件）：

`pdftoppm -mono {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成灰度PGM文件（而不是彩色PPM文件）：

`pdftoppm -gray {{path/to/file.pdf}} {{image_name_prefix}}`

- 生成PNG文件而不是PPM文件：

`pdftoppm -png {{path/to/file.pdf}} {{image_name_prefix}}`