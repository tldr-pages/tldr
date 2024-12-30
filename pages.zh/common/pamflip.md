# pamflip

> 翻转或旋转 PAM 或 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamflip.html>。

- 按指定角度逆时针旋转输入图像：

`pamflip -rotate{{90|180|270}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 左右翻转：

`pamflip -leftright {{path/to/input.pam}} > {{path/to/output.pam}}`

- 上下翻转：

`pamflip -topbottom {{path/to/input.pam}} > {{path/to/output.pam}}`

- 沿主对角线翻转输入图像：

`pamflip -transpose {{path/to/input.pam}} > {{path/to/output.pam}}`