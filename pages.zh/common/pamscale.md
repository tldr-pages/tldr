# pamscale

> 缩放 Netpbm 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamscale.html>。

- 缩放图像，使结果具有指定的尺寸：

`pamscale -width {{width}} -height {{height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 缩放图像，使结果具有指定的宽度，同时保持纵横比：

`pamscale -width {{width}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 缩放图像，使其宽度和高度分别按指定的比例变化：

`pamscale -xscale {{x_factor}} -yscale {{y_factor}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 缩放图像，使其在保持纵横比的情况下适合指定的边框大小：

`pamscale -xyfit {{bbox_width}} {{bbox_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 缩放图像，使其在保持纵横比的情况下完全填满指定的框：

`pamscale -xyfill {{box_width}} {{box_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`