# pngtopam

> 将 PNG 图像转换为 Netpbm 图像。
> 另见: `pamtopng`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pngtopam.html>。

- 将指定的 PNG 图像转换为 Netpbm 图像：

`pngtopam {{path/to/image.png}} > {{path/to/output.pam}}`

- 创建一个包含主图像和输入图像透明度蒙版的输出图像：

`pngtopam -alphapam {{path/to/image.png}} > {{path/to/output.pam}}`

- 用指定颜色替换透明像素：

`pngtopam -mix -background {{color}} {{path/to/image.png}} > {{path/to/output.pam}}`

- 将输入图像中找到的 tEXt 块写入指定的文本文件：

`pngtopam -text {{path/to/file.txt}} {{path/to/image.png}} > {{path/to/output.pam}}`