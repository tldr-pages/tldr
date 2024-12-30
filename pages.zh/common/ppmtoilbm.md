# ppmtoilbm

> 将PPM图像转换为ILBM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoilbm.html>。

- 将PPM图像转换为ILBM文件：

`ppmtoilbm {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 向ILBM文件写入最多n个平面，并在超过此数量时生成HAM/24位/直接颜色文件：

`ppmtoilbm -maxplanes {{n}} -{{hamif|24if|dcif}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 生成具有确切n个平面的ILBM文件：

`ppmtoilbm -fixplanes {{n}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 选择要使用的压缩方法：

`ppmtoilbm -{{compress|nocompress|savemem}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`