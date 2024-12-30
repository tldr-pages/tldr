# magick compare

> 创建一个比较图像，以直观地注释两个图像之间的差异。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/compare.php>。

- 比较两个图像：

`magick compare {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

- 使用指定的度量比较两个图像：

`magick compare -verbose -metric {{PSNR}} {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`