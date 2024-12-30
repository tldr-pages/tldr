# pnmgamma

> 对PNM图像执行伽玛校正。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmgamma.html>。

- 将图像从BT.709亮度转换为辐射或sRGB亮度：

`pnmgamma -{{bt709tolinear|bt709tosrgb}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 将图像从辐射或sRGB亮度转换为BT.709亮度：

`pnmgamma -{{lineartobt709|srgbtobt709}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 指定用于伽玛转换函数的伽玛值：

`pnmgamma -gamma {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 指定每个颜色分量用于伽玛转换函数的伽玛值：

`pnmgamma -rgamma {{value}} -ggamma {{value}} -bgamma {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`