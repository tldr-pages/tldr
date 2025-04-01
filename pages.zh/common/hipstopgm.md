# hipstopgm

> 读取 HIPS 文件作为输入，并返回 PGM 图像作为输出。
> 如果 HIPS 文件包含多个连续的帧，`hipstopgm` 会将所有帧垂直拼接。
> 更多信息：<https://netpbm.sourceforge.net/doc/hipstopgm.html>.

- 将 HIPS 文件转换为 PGM 图像：

`hipstopgm {{path/to/file.hips}}`

- 抑制所有信息性消息：

`hipstopgm -quiet`

- 显示版本：

`hipstopgm -version`
