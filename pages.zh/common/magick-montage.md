# magick montage

> 在可自定义的网格内平铺图片。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/montage.php>.

- 平铺图片，尺寸大于格子的图片将会被自动缩小：

`magick montage {{路径/到/图片1.jpg 路径/到/图片2.jpg ...}} {{路径/到/拼图图片.jpg}}`

- 平铺图片，根据最大的图片来计算格子大小：

`magick montage {{路径/到/图片1.jpg 路径/到/图片2.jpg ...}} -geometry {{+0+0}} {{路径/到/拼图图片.jpg}}`

- 平铺图片，根据指定的格子大小调整图片尺寸：

`magick montage {{路径/到/图片1.jpg 路径/到/图片2.jpg ...}} -geometry {{640x480+0+0}} {{路径/到/拼图图片.jpg}}`

- 指定格子的行列数，如果图片数量超出格子数，则会输出复数张图片：

`magick montage {{路径/到/图片1.jpg 路径/到/图片2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- 平铺图片，裁剪图片以充满格子：

`magick montage {{路径/到/图片1.jpg 路径/到/图片2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{路径/到/拼图图片.jpg}}`
