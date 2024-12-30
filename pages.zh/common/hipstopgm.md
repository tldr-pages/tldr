# hipstopgm

> 读取一个 HIPS 文件作为输入，并返回一个 PGM 图像作为输出。
> 如果 HIPS 文件包含多个帧，`hipstopgm` 将会将所有帧垂直连接在一起。
> 更多信息：<https://netpbm.sourceforge.net/doc/hipstopgm.html>。

- 将 HIPS 文件转换为 PGM 图像：

`hipstopgm {{path/to/file.hips}}`

- 抑制所有信息消息：

`hipstopgm -quiet`

- 显示版本：

`hipstopgm -version`