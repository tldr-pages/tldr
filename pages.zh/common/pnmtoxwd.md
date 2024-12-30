# pnmtoxwd

> 将PNM文件转换为X11窗口转储文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtoxwd.html>。

- 将PNM图像文件转换为XWD：

`pnmtoxwd {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- 以DirectColor格式生成输出：

`pnmtoxwd -directcolor {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- 将输出的颜色深度设置为b位：

`pnmtoxwd -pseudodepth {{b}} {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`