# pamenlarge

> 通过复制像素来放大 PAM 图像。
> 参见：`pbmreduce`，`pamditherbw`，`pbmpscale`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamenlarge.html>。

- 按指定的倍数放大指定的图像：

`pamenlarge -scale {{N}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- 按指定的水平和垂直倍数放大指定的图像：

`pamenlarge -xscale {{XN}} -yscale {{YN}} {{path/to/image.pam}} > {{path/to/output.pam}}`