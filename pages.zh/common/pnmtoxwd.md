# pnmtoxwd

> 将 PNM 文件转换为 X11 窗口转储文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtoxwd.html>。

- 将 PNM 图像文件转换为 XWD：

`pnmtoxwd {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- 以 DirectColor 格式生成输出：

`pnmtoxwd -directcolor {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- 将输出的颜色深度设置为 b 位：

`pnmtoxwd -pseudodepth {{b}} {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`