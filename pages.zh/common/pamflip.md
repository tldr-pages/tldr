# pamflip

> 翻转或旋转 PAM 或 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamflip.html>。

- 将输入图像逆时针旋转指定的角度：

`pamflip -rotate{{90|180|270}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 左右翻转图像：

`pamflip -leftright {{path/to/input.pam}} > {{path/to/output.pam}}`

- 上下翻转图像：

`pamflip -topbottom {{path/to/input.pam}} > {{path/to/output.pam}}`

- 沿主对角线翻转图像：

`pamflip -transpose {{path/to/input.pam}} > {{path/to/output.pam}}`