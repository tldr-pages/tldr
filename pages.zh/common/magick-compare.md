# magick compare

> 创建一个对比图像，以直观标注两幅图像之间的差异。
> 参见：`magick`。
> 更多信息：<https://imagemagick.org/script/compare.php>。

- 对比两幅图像：

`magick compare {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

- 使用指定的度量标准对比两幅图像：

`magick compare -verbose -metric {{PSNR}} {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`
