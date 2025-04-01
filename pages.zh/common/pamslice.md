# pamslice

> 从 PAM 图像中提取一行值。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamslice.html>.

- 以表格形式打印第 n 行像素的值：

`pamslice -row {{n}} {{path/to/image.pam}}`

- 以表格形式打印第 n 列像素的值：

`pamslice -column {{n}} {{path/to/image.pam}}`

- 仅考虑输入图像的第 m 个平面：

`pamslice -row {{n}} -plane {{m}} {{path/to/image.pam}}`

- 生成适合 `xmgr` 可视化的输出格式：

`pamslice -row {{n}} -xmgr {{path/to/image.pam}}`
