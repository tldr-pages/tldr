# pamslice

> 从PAM图像中提取一行值。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamslice.html>。

- 以表格形式打印第n行像素的值：

`pamslice -row {{n}} {{path/to/image.pam}}`

- 以表格形式打印第n列像素的值：

`pamslice -column {{n}} {{path/to/image.pam}}`

- 仅考虑输入图像的第m平面：

`pamslice -row {{n}} -plane {{m}} {{path/to/image.pam}}`

- 生成适合输入到`xmgr`进行可视化的格式输出：

`pamslice -row {{n}} -xmgr {{path/to/image.pam}}`