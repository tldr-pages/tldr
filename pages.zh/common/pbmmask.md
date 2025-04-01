# pbmmask

> 从常规位图创建一个掩码位图。
> 参见：`pambackground`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmmask.html>。

- 创建一个掩码位图，将背景与前景分开：

`pbmmask {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- 将生成的掩码扩展一个像素：

`pbmmask -expand {{path/to/image.pbm}} > {{path/to/output.pbm}}`
