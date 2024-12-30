# ppmntsc

> 将PPM图像中的RGB颜色与NTSC或PAL色彩系统兼容。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmntsc.html>。

- 使PPM图像中的RGB颜色与NTSC色彩系统兼容：

`ppmntsc {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 使PPM图像中的RGB颜色与PAL色彩系统兼容：

`ppmntsc --pal {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 将输入图像中的非法像素数量打印到`stderr`：

`ppmntsc --verbose {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 仅输出合法/非法/已修正像素，其他像素设置为黑色：

`ppmntsc --{{legalonly|illegalonly|correctedonly}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`