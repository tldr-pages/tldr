# pamshadedrelief

> 从高程图生成阴影浮雕图。
> 请参阅：`pamcrater`, `ppmrelief`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamshadedrelief.html>。

- 使用输入的图像作为高程图生成阴影浮雕图像：

`pamshadedrelief < {{path/to/input.pam}} > {{path/to/output.pam}}`

- 通过指定的系数对图像进行伽玛校正：

`pamshadedrelief -gamma {{factor}} < {{path/to/input.pam}} > {{path/to/output.pam}}`