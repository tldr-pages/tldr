# pamtotga

> 将 Netpbm 图像转换为 TrueVision Targa 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtotga.html>.

- 将 Netpbm 图像转换为 TrueVision Targa 文件：

`pamtotga {{path/to/file.pam}} > {{path/to/output.tga}}`

- 指定输出图像的颜色映射：

`pamtotga -{{cmap|cmap16|mono|rgb}} {{path/to/file.pam}} > {{path/to/output.tga}}`

- 显示版本：

`pamtotga -version`
