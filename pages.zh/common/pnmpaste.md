# pnmpaste

> 将一个 PNM 图像粘贴到另一个 PNM 图像中。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmpaste.html>。

- 将一个 PNM 图像粘贴到另一个 PNM 图像的指定坐标处：

`pnmpaste {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`

- 将从 `stdin` 读取的图像粘贴到指定图像中：

`{{command}} | pnmpaste {{x}} {{y}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 通过指定的布尔运算组合重叠的像素，其中白色像素表示 `true`，黑色像素表示 `false`：

`pnmpaste -{{and|nand|or|nor|xor|xnor}} {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`