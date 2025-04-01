# pgmtexture

> 从 PGM 图像中提取纹理特征。
> 更多信息：<https://netpbm.sourceforge.net/doc/pgmtexture.html>.

- 从 PGM 图像中提取纹理特征：

`pgmtexture {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- 指定特征提取算法的距离参数：

`pgmtexture -d {{distance}} {{path/to/image.pgm}} > {{path/to/output.pgm}}`