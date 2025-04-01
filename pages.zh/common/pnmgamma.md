# pnmgamma

> 对 PNM 图像进行伽玛校正。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmgamma.html>.

- 将图像从 BT.709 亮度转换为辐射度或 sRGB 亮度：

`pnmgamma -{{bt709tolinear|bt709tosrgb}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 将图像从辐射度或 sRGB 亮度转换为 BT.709 亮度：

`pnmgamma -{{lineartobt709|srgbtobt709}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 指定用于伽玛传递函数的伽玛值：

`pnmgamma -gamma {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 为每个颜色分量指定用于伽玛传递函数的伽玛值：

`pnmgamma -rgamma {{value}} -ggamma {{value}} -bgamma {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`