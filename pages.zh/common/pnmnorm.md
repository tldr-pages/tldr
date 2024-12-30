# pnmnorm

> 规范化 PNM 图像的对比度。
> 另见：`pnmhisteq`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmnorm.html>。

- 强制最亮的像素为白色，最暗的像素为黑色，并线性分布中间的像素：

`pnmnorm {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 强制最亮的像素为白色，最暗的像素为黑色，并以平方方式分布中间的像素，使亮度为 `n` 的像素变为 50% 明亮：

`pnmnorm -midvalue {{n}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 保持像素的色调，仅修改亮度：

`pnmnorm -keephues {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 指定计算像素亮度的方法：

`pnmnorm -{{luminosity|colorvalue|saturation}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`