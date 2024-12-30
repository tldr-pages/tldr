# pnmconvol

> 对PNM图像进行卷积。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmconvol.html>。

- 使用指定的卷积矩阵对PNM图像进行卷积：

`pnmconvol -matrix=-1,3,-1 {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 使用指定文件中的卷积矩阵对PNM图像进行卷积，每个输入图像的层对应一个文件：

`pnmconvol -matrixfile {{path/to/matrix1,path/to/matrix2,...}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 使用指定的PNM文件中的卷积矩阵对PNM图像进行卷积：

`pnmconvol {{path/to/matrix.pnm}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 对卷积矩阵中的权重进行归一化，使它们的总和为1：

`pnmconvol -matrix=-1,3,-1 -normalize {{path/to/image.pnm}} > {{path/to/output.pnm}}`