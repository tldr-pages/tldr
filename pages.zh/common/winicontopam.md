# winicontopam

> 将 Windows ICO 文件转换为 PAM 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/winicontopam.html>。

- 读取 ICO 文件，并将其中的最佳质量图像转换为 PAM 格式：

`winicontopam {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 将输入文件中的所有图像转换为 PAM：

`winicontopam -allimages {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 将输入文件中的第 n 个图像转换为 PAM：

`winicontopam -image {{n}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 如果要提取的图像包含分级透明度数据和 AND 掩码，将 AND 掩码写入输出 PAM 文件的第五通道：

`winicontopam -andmasks {{path/to/input_file.ico}} > {{path/to/output.pam}}`
