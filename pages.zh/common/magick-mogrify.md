# magick mogrify

> 对多个图像执行操作，如调整大小、裁剪、翻转和添加效果。
> 更改将直接应用于原文件。
> 详见：`magick`。
> 更多信息：<https://imagemagick.org/script/mogrify.php>。

- 将目录中的所有 JPEG 图像调整为原始大小的 50%：

`magick mogrify -resize {{50%}} {{*.jpg}}`

- 将所有以 `DSC` 开头的图像调整为 800x600：

`magick mogrify -resize {{800x600}} {{DSC*}}`

- 将目录中的所有 PNG 图像转换为 JPEG：

`magick mogrify -format {{jpg}} {{*.png}}`

- 将当前目录中的所有图像文件的饱和度减半：

`magick mogrify -modulate {{100,50}} {{*}}`

- 将当前目录中的所有图像文件的亮度加倍：

`magick mogrify -modulate {{200}} {{*}}`

- 通过降低质量来减少当前目录中所有 GIF 图像的文件大小：

`magick mogrify -layers 'optimize' -fuzz {{7%}} {{*.gif}}`

- 显示帮助：

`magick mogrify -help`
