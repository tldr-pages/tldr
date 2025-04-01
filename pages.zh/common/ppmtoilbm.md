# ppmtoilbm

> 将 PPM 图像转换为 ILBM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoilbm.html>.

- 将 PPM 图像转换为 ILBM 文件：

`ppmtoilbm {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 将最多 n 个平面写入 ILBM 文件，如果超过该数量，则生成 HAM/24 位/直接颜色文件：

`ppmtoilbm -maxplanes {{n}} -{{hamif|24if|dcif}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 生成具有正好 n 个平面的 ILBM 文件：

`ppmtoilbm -fixplanes {{n}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- 选择要使用的压缩方法：

`ppmtoilbm -{{compress|nocompress|savemem}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`
