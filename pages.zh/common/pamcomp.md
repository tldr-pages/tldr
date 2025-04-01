# pamcomp

> 叠加两个 PAM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamcomp.html>.

- 将两个图像叠加，使上层图像遮挡下层图像的部分区域：

`pamcomp {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置上层图像的水平对齐方式：

`pamcomp -align {{left|center|right|beyondleft|beyondright}} -xoff {{x_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置上层图像的垂直对齐方式：

`pamcomp -valign {{top|middle|bottom|above|below}} -yoff {{y_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置上层图像的不透明度：

`pamcomp -opacity {{0.7}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`
