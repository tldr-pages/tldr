# magick convert

> 在不同图像格式之间转换、缩放、合并和创建图像等。
> 注意：此工具（之前为 `convert`）在 ImageMagick 7+ 版本中已被 `magick` 取代。
> 更多信息：<https://imagemagick.org/script/convert.php>.

- 将图像从 JPEG 转换为 PNG：

`magick convert {{path/to/input_image.jpg}} {{path/to/output_image.png}}`

- 将图像缩放为其原始大小的 50%：

`magick convert {{path/to/input_image.png}} -resize 50% {{path/to/output_image.png}}`

- 将图像按原始长宽比缩放至最大尺寸 640x480：

`magick convert {{path/to/input_image.png}} -resize 640x480 {{path/to/output_image.png}}`

- 将图像缩放至指定文件大小：

`magick convert {{path/to/input_image.png}} -define jpeg:extent=512kb {{path/to/output_image.jpg}}`

- 垂直/水平拼接图像：

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{-append|+append}} {{path/to/output_image.png}}`

- 从一系列图像中创建一个每帧间隔 100 毫秒的 GIF 动画：

`magick convert {{path/to/image1.png path/to/image2.png ...}} -delay {{10}} {{path/to/animation.gif}}`

- 创建一个纯红色背景的图像：

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{path/to/image.png}}`

- 从不同尺寸的多个图像创建一个 favicon：

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{path/to/favicon.ico}}`
