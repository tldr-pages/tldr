# exif

> 显示和更改JPEG文件中的EXIF信息。
> 更多信息：<https://github.com/libexif/exif/>。

- 显示图像中所有识别的EXIF信息：

`exif {{path/to/image.jpg}}`

- 显示一个表格，列出已知的EXIF标签以及每个标签在图像中是否存在：

`exif --list-tags --no-fixup {{image.jpg}}`

- 将图像缩略图提取到文件`thumbnail.jpg`中：

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{image.jpg}}`

- 显示给定图像中“Model”标签的原始内容：

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{image.jpg}}`

- 将“Artist”标签的值更改为John Smith，并保存为`new.jpg`：

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{image.jpg}}`