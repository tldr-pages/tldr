# pampop9

> 模拟一个多镜头相机，如 Pop9。
> 更多信息：<https://netpbm.sourceforge.net/doc/pampop9.html>。

- 将输入图像平铺为 xtiles 行和 ytiles 列，每次根据 xdelta 和 ydelta 增加偏移量：

`pampop9 {{path/to/input.pam}} {{xtiles}} {{ytiles}} {{xdelta}} {{ydelta}} > {{path/to/output.pam}}`