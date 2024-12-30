# yuvsplittoppm

> 将三个降采样的Abekas YUV文件转换为一个PPM图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/yuvsplittoppm.html>。

- 从三个以basename开头的文件中读取Akebas YUV字节，将它们合并为一个PPM图像，并将其存储在指定的输出文件中：

`yuvsplittoppm {{basename}} {{width}} {{height}} > {{path/to/output_file.ppm}}`