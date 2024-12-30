# magick mogrify

> 对多个图像执行操作，例如调整大小、裁剪、翻转和添加效果。
> 更改直接应用于原始文件。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/mogrify.php>。

- 将目录中所有JPEG图像的大小调整为其初始大小的50%：

`magick mogrify -resize {{50%}} {{*.jpg}}`

- 将所有以`DSC`开头的图像调整为800x600：

`magick mogrify -resize {{800x600}} {{DSC*}}`

- 将目录中所有PNG图像转换为JPEG：

`magick mogrify -format {{jpg}} {{*.png}}`

- 将当前目录中所有图像文件的饱和度降低一半：

`magick mogrify -modulate {{100,50}} {{*}}`

- 将当前目录中所有图像文件的亮度加倍：

`magick mogrify -modulate {{200}} {{*}}`

- 通过降低质量来减少当前目录中所有GIF图像的文件大小：

`magick mogrify -layers 'optimize' -fuzz {{7%}} {{*.gif}}`