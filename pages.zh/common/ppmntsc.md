# ppmntsc

> 使 PPM 图像中的 RGB 颜色与 NTSC 或 PAL 色彩系统兼容。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmntsc.html>.

- 使 PPM 图像中的 RGB 颜色与 NTSC 色彩系统兼容：

`ppmntsc {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 使 PPM 图像中的 RGB 颜色与 PAL 色彩系统兼容：

`ppmntsc --pal {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 将输入图像中的非法像素数量输出到 `stderr`：

`ppmntsc --verbose {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- 只输出合法/非法/修正后的像素，将其他像素设置为黑色：

`ppmntsc --{{legalonly|illegalonly|correctedonly}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
