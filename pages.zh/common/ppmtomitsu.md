# ppmtomitsu

> 将PPM图像转换为三菱S340-10文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtomitsu.html>。

- 将PPM图像转换为MITSU文件：

`ppmtomitsu {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- 按指定倍数放大图像，使用指定的锐度并生成`n`个副本：

`ppmtomitsu -enlarge {{1|2|3}} -sharpness {{1|2|3|4}} -copy {{n}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- 使用指定的介质进行打印过程：

`ppmtomitsu -media {{A|A4|AS|A4S}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`