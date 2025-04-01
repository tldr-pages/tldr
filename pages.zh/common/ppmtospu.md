# ppmtospu

> 将 PPM 文件转换为 Atari Spectrum 512 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtospu.html>.

- 将 PPM 文件转换为 Atari Spectrum 512 图像：

`ppmtospu {{path/to/input.ppm}} > {{path/to/output.spu}}`

- 使用指定大小的抖动矩阵（0 表示不使用抖动）：

`ppmtospu -d{{0|2|4}} {{path/to/input.ppm}} > {{path/to/output.spu}}`
