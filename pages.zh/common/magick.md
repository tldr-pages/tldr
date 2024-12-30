# magick

> 创建、编辑、组合或转换图像格式。
> 此工具替代了ImageMagick 7+中的 `convert`。请使用 `magick convert` 在7+版本中使用旧工具。
> 一些子命令，例如 `mogrify`，有自己的使用文档。
> 更多信息：<https://imagemagick.org>。

- 在图像格式之间转换：

`magick {{path/to/input_image.png}} {{path/to/output_image.jpg}}`

- 调整图像大小，制作新副本：

`magick {{path/to/input_image.jpg}} -resize {{100x100}} {{path/to/output_image.jpg}}`

- 从当前目录中的所有JPEG图像创建GIF：

`magick {{*.jpg}} {{path/to/images.gif}}`

- 创建棋盘图案：

`magick -size {{640x480}} pattern:checkerboard {{path/to/checkerboard.png}}`

- 从当前目录中的所有JPEG图像创建PDF文件：

`magick {{*.jpg}} -adjoin {{path/to/file.pdf}}`