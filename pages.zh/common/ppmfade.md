# ppmfade

> 生成两个 PPM 图像之间的过渡。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmfade.html>.

- 使用指定效果生成两个 PPM 图像（[f]irst 和 [l]ast）之间的过渡：

`ppmfade -f {{path/to/image1.ppm}} -l {{path/to/image2.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 生成从指定图像开始，以纯黑色图像结束的过渡：

`ppmfade -f {{path/to/image.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 生成从纯黑色图像开始，以指定图像结束的过渡：

`ppmfade -l {{path/to/image.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 将结果图像存储在名为 `base.NNNN.ppm` 的文件中，其中 `NNNN` 是一个递增的数字：

`ppmfade -f {{path/to/image1.ppm}} -l {{path/to/image2.ppm}} -{{mix|spread|shift|relief|oil|...}} -base {{base}}`
