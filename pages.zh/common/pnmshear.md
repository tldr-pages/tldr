# pnmshear

> 剪切 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmshear.html>。

- 按指定角度剪切 PNM 图像：

`pnmshear {{角度}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`

- 指定剪切图像的背景颜色：

`pnmshear -background {{蓝色}} {{角度}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`

- 不执行抗锯齿处理：

`pnmshear -noantialias {{角度}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`