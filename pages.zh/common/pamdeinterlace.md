# pamdeinterlace

> 从 Netpbm 图像中删除每隔一行。
> 另见: `pammixinterlace`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>。

- 生成一个由输入的偶数行组成的图像：

`pamdeinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 生成一个由输入的奇数行组成的图像：

`pamdeinterlace -takeodd {{path/to/image.ppm}} > {{path/to/output.ppm}}`