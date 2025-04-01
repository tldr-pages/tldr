# magick

> 创建、编辑、组合或转换图像格式。
> 从 ImageMagick 7+ 版本开始，此工具取代了 `convert`。在 7+ 版本中使用旧工具，可以参见 `magick convert`。
> 一些子命令，如 `mogrify` 有自己的使用文档。
> 更多信息：<https://imagemagick.org>.

- 在图像格式之间进行转换：

`magick {{path/to/input_image.png}} {{path/to/output_image.jpg}}`

- 调整图像大小，创建一个新的副本：

`magick {{path/to/input_image.jpg}} -resize {{100x100}} {{path/to/output_image.jpg}}`

- 将当前目录中的所有 JPEG 图像组合成一个 GIF：

`magick {{*.jpg}} {{path/to/images.gif}}`

- 创建一个棋盘图案：

`magick -size {{640x480}} pattern:checkerboard {{path/to/checkerboard.png}}`

- 将当前目录中的所有 JPEG 图像组合成一个 PDF 文件：

`magick {{*.jpg}} -adjoin {{path/to/file.pdf}}`