# magick montage

> 将图像拼接成可自定义的网格。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/montage.php>。

- 将图像拼接成网格，自动调整大于网格单元大小的图像：

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} {{path/to/montage.jpg}}`

- 将图像拼接成网格，自动根据最大图像计算网格单元大小：

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} {{path/to/montage.jpg}}`

- 指定网格单元大小，并在拼接前调整图像以适应它：

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{640x480+0+0}} {{path/to/montage.jpg}}`

- 限制网格中的行数和列数，导致输入图像溢出到多个输出拼接图中：

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- 在拼接前调整大小并裁剪图像以填充其网格单元：

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{path/to/montage.jpg}}`