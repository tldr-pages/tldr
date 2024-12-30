# magick convert

> 在图像格式之间转换、缩放、合并、创建图像，等等。
> 注意：该工具（之前称为`convert`）在 ImageMagick 7+ 中已被 `magick` 替代。
> 更多信息：<https://imagemagick.org/script/convert.php>。

- 将图像从 JPEG 转换为 PNG：

`magick convert {{path/to/input_image.jpg}} {{path/to/output_image.png}}`

- 将图像缩放到原始大小的 50%：

`magick convert {{path/to/input_image.png}} -resize 50% {{path/to/output_image.png}}`

- 将图像缩放，保持原始长宽比，最大尺寸为 640x480：

`magick convert {{path/to/input_image.png}} -resize 640x480 {{path/to/output_image.png}}`

- 将图像缩放到指定的文件大小：

`magick convert {{path/to/input_image.png}} -define jpeg:extent=512kb {{path/to/output_image.jpg}}`

- 垂直/水平拼接图像：

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{-append|+append}} {{path/to/output_image.png}}`

- 从一系列图像创建 GIF，图像之间延迟 100 毫秒：

`magick convert {{path/to/image1.png path/to/image2.png ...}} -delay {{10}} {{path/to/animation.gif}}`

- 创建一幅只有纯红色背景的图像：

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{path/to/image.png}}`

- 从几张不同尺寸的图像创建一个 favicon：

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{path/to/favicon.ico}}`