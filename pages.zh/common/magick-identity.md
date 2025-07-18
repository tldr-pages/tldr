# magick identify

> 输出图片文件的格式与属性。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/identify.php>.

- 输出图片的格式以及一些基本属性：

`magick identify {{路径/到/图片}}`

- 输出图片的格式及其详细属性：

`magick identify -verbose {{路径/到/图片}}`

- 将当前目录下的所有 JPEG 图片的尺寸属性：

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{路径/到/文件列表.csv}}`
