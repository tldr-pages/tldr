# pamtowinicon

> 将 PAM 图像转换为 Windows ICO 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- 将 PAM 图像文件转换为 ICO 文件：

`pamtowinicon {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- 将分辨率小于 t 的图像编码为 BMP 格式，其他所有图像编码为 PNG 格式：

`pamtowinicon -pngthreshold {{t}} {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- 将非不透明区域外的所有像素变为黑色：

`pamtowinicon -truetransparent {{path/to/input_file.pam}} > {{path/to/output.ico}}`
