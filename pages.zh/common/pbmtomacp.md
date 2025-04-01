# pbmtomacp

> 将 PBM 图像转换为 MacPaint 文件。
> 参见：`macptopbm`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtomacp.html>。

- 将 PBM 图像转换为 MACP 文件：

`pbmtomacp {{path/to/image.pbm}} > {{path/to/output.macp}}`

- 不对输出文件进行压缩：

`pbmtomacp -norle {{path/to/image.pbm}} > {{path/to/output.macp}}`