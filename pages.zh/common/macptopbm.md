# macptopbm

> 读取MacPaint文件作为输入，并生成PBM图像作为输出。
> 另请参见: `pbmtomacp`。
> 更多信息: <https://netpbm.sourceforge.net/doc/macptopbm.html>。

- 将MacPaint文件转换为PGM图像：

`macptopbm {{path/to/file.macp}} > {{path/to/output.pbm}}`

- 在读取文件时跳过指定数量的字节：

`macptopbm -extraskip {{N}} > {{path/to/output.pbm}}`

- 抑制所有信息消息：

`macptopbm -quiet > {{path/to/output.pbm}}`

- 显示版本：

`macptopbm -version`