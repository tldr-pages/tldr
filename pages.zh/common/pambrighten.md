# pambrighten

> 调整 PAM 图像的饱和度和亮度。
> 更多信息：<https://netpbm.sourceforge.net/doc/pambrighten.html>.

- 按指定的百分比增加每个像素的饱和度：

`pambrighten -saturation {{value_percent}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- 按指定的百分比增加每个像素的亮度（HSV 颜色空间中的值）：

`pambrighten -value {{value_percent}} {{path/to/image.pam}} > {{path/to/output.pam}}`