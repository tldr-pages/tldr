# pamdeinterlace

> 删除 Netpbm 图像中的每隔一行。
> 参见：`pammixinterlace`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamdeinterlace.html>。

- 生成一个由输入图像的偶数行组成的新图像：

`pamdeinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 生成一个由输入图像的奇数行组成的新图像：

`pamdeinterlace -takeodd {{path/to/image.ppm}} > {{path/to/output.ppm}}`
