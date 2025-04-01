# exif

> 显示和更改 JPEG 文件中的 EXIF 信息。
> 更多信息：<https://github.com/libexif/exif/>.

- 显示图像中所有识别的 EXIF 信息：

`exif {{path/to/image.jpg}}`

- 以表格形式列出已知的 EXIF 标签及其在图像中的存在情况：

`exif --list-tags --no-fixup {{image.jpg}}`

- 将图像缩略图提取到 `thumbnail.jpg` 文件中：

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{image.jpg}}`

- 显示给定图像中 "Model" 标签的原始内容：

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{image.jpg}}`

- 将 "Artist" 标签的值更改为 John Smith 并保存到 `new.jpg`：

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{image.jpg}}`
