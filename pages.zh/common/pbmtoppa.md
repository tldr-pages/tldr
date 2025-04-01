# pbmtoppa

> 将 PBM 图像转换为 HP 打印机性能架构格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoppa.html>.

- 将 PBM 图像转换为 PPA 文件：

`pbmtoppa {{path/to/image.pbm}} > {{path/to/output.ppa}}`

- 指定所需的每英寸点数和纸张大小：

`pbmtoppa -d {{300}} -s {{a4}} {{path/to/image.pbm}} > {{path/to/output.ppa}}`