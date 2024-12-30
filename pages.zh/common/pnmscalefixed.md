# pnmscalefixed

> 快速缩放 PNM 文件，可能会降低质量。
> 另见：`pamscale`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmscalefixed.html>。

- 缩放图像，使结果具有指定的尺寸：

`pnmscalefixed -width {{宽度}} -height {{高度}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`

- 缩放图像，使结果具有指定的宽度，保持纵横比：

`pnmscalefixed -width {{宽度}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`

- 缩放图像，使其宽度和高度按指定的比例变化：

`pnmscalefixed -xscale {{x_因子}} -yscale {{y_因子}} {{输入.pnm 的路径}} > {{输出.pnm 的路径}}`