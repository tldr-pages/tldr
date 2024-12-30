# ppmtosixel

> 将 PPM 图像转换为 DEC sixel 格式。
> 更多信息请访问: <https://netpbm.sourceforge.net/doc/ppmtosixel.html>。

- 将 PPM 图像转换为 DEC sixel 格式：

`ppmtosixel {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- 生成一个未压缩的 SIXEL 文件，打印速度较慢：

`ppmtosixel -raw {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- 添加 1.5 英寸的左边距：

`ppmtosixel -margin {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- 以更便携（虽然占用空间效率较低）的方法编码控制代码：

`ppmtosixel -7bit {{path/to/file.ppm}} > {{path/to/file.sixel}}`