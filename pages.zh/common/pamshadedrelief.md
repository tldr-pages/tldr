# pamshadedrelief

> 从高程图生成阴影浮雕图像。
> 另请参见：`pamcrater`，`ppmrelief`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamshadedrelief.html>。

- 生成一个阴影浮雕图像，输入图像被解释为高程图：

`pamshadedrelief < {{path/to/input.pam}} > {{path/to/output.pam}}`

- 按指定因子对图像进行伽玛调整：

`pamshadedrelief -gamma {{factor}} < {{path/to/input.pam}} > {{path/to/output.pam}}`