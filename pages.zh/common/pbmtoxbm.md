# pbmtoxbm

> 将 PBM 图像转换为 X11 或 X10 位图。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- 将 PBM 图像转换为 X11 XBM 文件：

`pbmtoxbm {{path/to/input_file.pbm}} > {{path/to/output_file.xbm}}`

- 明确指定生成 X11 或 X10 位图：

`pbmtoxbm -{{x11|x10}} {{path/to/input_file.pbm}} > {{path/to/output_file.xbm}}`