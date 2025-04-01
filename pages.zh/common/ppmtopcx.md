# ppmtopcx

> 将 PPM 图像转换为 PCX 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtopcx.html>。

- 将 PPM 图像转换为 PCX 文件：

`ppmtopcx {{path/to/file.ppm}} > {{path/to/file.pcx}}`

- 生成具有指定颜色深度的 PCX 文件：

`ppmtopcx -{{8bit|24bit}} {{path/to/file.ppm}} > {{path/to/file.pcx}}`
