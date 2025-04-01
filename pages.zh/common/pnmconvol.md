# pnmconvol

> 对 PNM 图像进行卷积操作。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmconvol.html>.

- 使用指定的卷积矩阵对 PNM 图像进行卷积操作：

`pnmconvol -matrix=-1,3,-1 {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 使用指定文件中的卷积矩阵对 PNM 图像进行卷积操作，每个输入图像层对应一个矩阵文件：

`pnmconvol -matrixfile {{path/to/matrix1,path/to/matrix2,...}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 使用指定的 PNM 文件中的卷积矩阵对 PNM 图像进行卷积操作：

`pnmconvol {{path/to/matrix.pnm}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 归一化卷积矩阵中的权重，使其总和为一：

`pnmconvol -matrix=-1,3,-1 -normalize {{path/to/image.pnm}} > {{path/to/output.pnm}}`