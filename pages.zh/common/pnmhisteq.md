# pnmhisteq

> 对PNM图像进行直方图均衡。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmhisteq.html>。

- 使用直方图均衡增加PNM图像的对比度：

`pnmhisteq {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 仅修改灰度像素：

`pnmhisteq -grey {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 在直方图均衡时不包括黑色或白色像素：

`pnmhisteq -no{{black|white}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`