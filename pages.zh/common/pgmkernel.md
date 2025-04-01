# pgmkernel

> 生成一个用于 `pnmconvol` 的卷积核。
> 参见：`pnmconvol`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmkernel.html>。

- 生成一个卷积核：

`pgmkernel {{width}} {{height}} > {{path/to/output.pgm}}`

- 生成一个平方卷积核：

`pgmkernel {{size}} > {{path/to/output.pgm}}`

- 指定生成的卷积核中心的权重：

`pgmkernel -weight {{value}} {{width}} {{height}} > {{path/to/output.pgm}}`