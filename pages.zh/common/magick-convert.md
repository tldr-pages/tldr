# magick convert

> 转换图片格式，创建，组合图片，调整图片尺寸等功能。
> 注意：原命令 `convert` 在 ImageMagick 7 以上版本中已被替换为 `magick`。
> 更多信息：<https://imagemagick.org/script/convert.php>.

- 将 JPEG 图片转换为 PNG 图片：

`magick convert {{路径/到/输入图片.jpg}} {{路径/到/输出图片.png}}`

- 将图片调整至原图片尺寸的50%：

`magick convert {{路径/到/输入图片.png}} -resize 50% {{路径/到/输出图片.png}}`

- 在宽高都不超过 640x480 的限制下，保持图片的比例，将尺寸调整至最大：

`magick convert {{路径/到/输入图片.png}} -resize 640x480 {{路径/到/输出图片.png}}`

- 将图片调整至特定文件大小：

`magick convert {{路径/到/输入图片.png}} -define jpeg:extent=512kb {{路径/到/输出图片.jpg}}`

- 水平/竖直地排列图片：

`magick convert -background none {{路径/到/图片1.png 路径/到/图片2.png ...}} {{-append|+append}} {{路径/到/输出图片.png}}`

- 创建一个 GIF 动图，按 100ms 的间隔播放一系列图片：

`magick convert {{路径/到/图片1.png 路径/到/图片2.png ...}} -delay {{10}} {{路径/到/GIF 动图.gif}}`

- 创建一个纯红背景的空白图片：

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{路径/到/图片.png}}`

- 通过若干不同尺寸的图片生成一个 favicon：

`magick convert {{路径/到/图片1.png 路径/到/图片2.png ...}} {{路径/到/网站图标.icon}}`
