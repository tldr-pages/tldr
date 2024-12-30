# pamstretch

> 通过在像素之间插值来放大PAM图像。
> 另见: `pamstretch-gen`, `pamenlarge`, `pamscale`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pamstretch.html>。

- 按整数因子放大PAM图像：

`pamstretch {{N}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- 按指定的水平和垂直方向因子放大PAM图像：

`pamstretch -xscale {{XN}} -yscale {{YN}} {{path/to/image.pam}} > {{path/to/output.pam}}`