# pamstretch

> 通过像素插值放大 PAM 图像。
> 参见：`pamstretch-gen`, `pamenlarge`, `pamscale`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamstretch.html>。

- 按整数倍放大 PAM 图像：

`pamstretch {{n}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- 在水平和垂直方向上按指定倍数放大 PAM 图像：

`pamstretch -xscale {{xn}} -yscale {{yn}} {{path/to/image.pam}} > {{path/to/output.pam}}`