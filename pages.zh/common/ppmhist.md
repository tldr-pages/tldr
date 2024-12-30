# ppmhist

> 打印PPM图像中存在的颜色直方图。
> 另见：`pgmhist`。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmhist.html>。

- 生成供人类阅读的直方图：

`ppmhist -nomap {{path/to/image.ppm}}`

- 生成图像的颜色映射的PPM文件，并将颜色直方图作为注释：

`ppmhist -map {{path/to/image.ppm}}`

- 显示版本：

`ppmhist -version`