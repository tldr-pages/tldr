# pgmkernel

> 生成一个用于 `pnmconvol` 的卷积核。
> 另见： `pnmconvol`。
> 更多信息： <https://netpbm.sourceforge.net/doc/pgmkernel.html>。

- 生成一个卷积核：

`pgmkernel {{宽度}} {{高度}} > {{输出.pgm的路径}}`

- 生成一个平方卷积核：

`pgmkernel {{大小}} > {{输出.pgm的路径}}`

- 指定生成的卷积核中中心的权重：

`pgmkernel -weight {{值}} {{宽度}} {{高度}} > {{输出.pgm的路径}}`