# pnmshear

> 剪切 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmshear.html>.

- 按指定角度剪切 PNM 图像：

`pnmshear {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 指定剪切后图像的背景颜色：

`pnmshear -background {{blue}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 不进行抗锯齿处理：

`pnmshear -noantialias {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`