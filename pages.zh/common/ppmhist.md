# ppmhist

> 打印 PPM 图像中出现的颜色的直方图。
> 参见：`pgmhist`。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmhist.html>。

- 生成可读的直方图：

`ppmhist -nomap {{path/to/image.ppm}}`

- 生成图像的调色板 PPM 文件，并将颜色直方图作为注释：

`ppmhist -map {{path/to/image.ppm}}`

- 显示版本：

`ppmhist -version`
