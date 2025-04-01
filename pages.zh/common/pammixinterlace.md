# pammixinterlace

> 将图像中的每一行与它的两个邻行合并。
> 参见: `pamdeinterlace`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>。

- 将图像中的每一行与它的两个邻行合并：

`pammixinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 使用指定的滤波机制：

`pammixinterlace -filter {{linear|fir|ffmpeg}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 开启自适应滤波模式，即仅修改明显属于梳状图案的像素：

`pammixinterlace -adaptive {{path/to/image.ppm}} > {{path/to/output.ppm}}`
