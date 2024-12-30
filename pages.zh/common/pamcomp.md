# pamcomp

> 叠加两幅 PAM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamcomp.html>。

- 叠加两幅图像，使叠加图像覆盖底图的部分：

`pamcomp {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置叠加图像的水平对齐方式：

`pamcomp -align {{left|center|right|beyondleft|beyondright}} -xoff {{x_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置叠加图像的垂直对齐方式：

`pamcomp -valign {{top|middle|bottom|above|below}} -yoff {{y_offset}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`

- 设置叠加图像的透明度：

`pamcomp -opacity {{0.7}} {{path/to/overlay.pam}} {{path/to/underlay.pam}} > {{path/to/output.pam}}`