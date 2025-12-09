# magick mogrify

> 对图片进行调整尺寸，裁剪旋转或添加效果等操作。
> 修改直接作用于原文件。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/mogrify.php>.

- 将当前目录下所有 JPEG 图片的尺寸都调整至原尺寸的 50%：

`magick mogrify -resize {{50%}} {{*.jpg}}`

- 将当前目录下所有以 DSC 开头的图片尺寸都调整至 800x600：

`magick mogrify -resize {{800x600}} {{DSC*}}`

- 将当前目录下所有 PNG 图片都转换为 JPEG 图片：

`magick mogrify -format {{jpg}} {{*.png}}`

- 将当前目录下所有图片文件的饱和度都减半：

`magick mogrify -modulate {{100,50}} {{*}}`

- 将当前目录下所有图片文件的亮度都加倍：

`magick mogrify -modulate {{200}} {{*}}`

- 通过降低图像品质，缩小当前目录下所有 GIF 动图的文件大小：

`magick mogrify -layers 'optimize' -fuzz {{7%}} {{*.gif}}`

- 查看帮助：

`magick mogrify -help`
