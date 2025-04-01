# pbmtogem

> 读取 PBM 图像作为输入，并生成压缩的 GEM .img 文件作为输出。
> `pbmtogem` 无法压缩重复的行。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtogem.html>。

- 将 PBM 图像转换为 GEM .img 文件：

`pbmtogem {{path/to/file.pbm}} > {{path/to/file.img}}`

- 抑制所有信息消息：

`pbmtogem -quiet`

- 显示版本：

`pbmtogem -version`
