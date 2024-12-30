# pammixinterlace

> 将图像中的每一行与其两个邻居合并。
> 另见：`pamdeinterlace`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pammixinterlace.html>。

- 将图像中的每一行与其两个邻居合并：

`pammixinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 使用指定的滤波机制：

`pammixinterlace -filter {{linear|fir|ffmpeg}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 开启自适应滤波模式，即只修改明显属于梳状图案的像素：

`pammixinterlace -adaptive {{path/to/image.ppm}} > {{path/to/output.ppm}}`