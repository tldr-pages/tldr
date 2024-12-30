# pambrighten

> 更改PAM图像的饱和度和明度。
> 更多信息：<https://netpbm.sourceforge.net/doc/pambrighten.html>。

- 按指定的百分比增加每个像素的饱和度：

`pambrighten -saturation {{value_percent}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- 按指定的百分比增加每个像素的明度（来自HSV颜色空间）：

`pambrighten -value {{value_percent}} {{path/to/image.pam}} > {{path/to/output.pam}}`