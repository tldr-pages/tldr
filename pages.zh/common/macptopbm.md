# macptopbm

> 读取 MacPaint 文件作为输入，并生成 PBM 图像作为输出。
> 另请参阅: `pbmtomacp`。
> 更多信息: <https://netpbm.sourceforge.net/doc/macptopbm.html>。

- 将 MacPaint 文件转换为 PGM 图像：

`macptopbm {{path/to/file.macp}} > {{path/to/output.pbm}}`

- 读取文件时跳过 `n` 个字节：

`macptopbm -extraskip {{n}} > {{path/to/output.pbm}}`

- 抑制所有信息性消息：

`macptopbm -quiet > {{path/to/output.pbm}}`

- 显示版本信息：

`macptopbm -version`