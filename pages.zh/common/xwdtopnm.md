# xwdtopnm

> 将 X11 或 X10 窗口转储文件转换为 PNM。
> 更多信息：<https://netpbm.sourceforge.net/doc/xwdtopnm.html>。

- 将 XWD 图像文件转换为 PBM：

`xwdtopnm {{path/to/input_file.xwd}} > {{path/to/output_file.pbm}}`

- 显示转换过程的信息：

`xwdtopnm -verbose {{path/to/input_file.xwd}} > {{path/to/output_file.pnm}}`

- 显示输入文件的 X11 标头内容：

`xwdtopnm -headerdump {{path/to/input_file.xwd}} > {{path/to/output_file.pnm}}`
