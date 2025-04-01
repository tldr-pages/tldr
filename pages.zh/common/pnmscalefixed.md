# pnmscalefixed

> 快速缩放PNM文件，可能会降低质量。
> 参见: `pamscale`。
> 更多信息: <https://netpbm.sourceforge.net/doc/pnmscalefixed.html>。

- 将图像缩放至指定的尺寸：

`pnmscalefixed -width {{width}} -height {{height}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 将图像缩放至指定的宽度，保持纵横比：

`pnmscalefixed -width {{width}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 按指定的因子改变图像的宽度和高度：

`pnmscalefixed -xscale {{x_factor}} -yscale {{y_factor}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
