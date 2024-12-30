# winicontopam

> 将Windows ICO文件转换为PAM文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/winicontopam.html>。

- 读取ICO文件并将其中包含的最佳质量图像转换为PAM格式：

`winicontopam {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 将输入文件中的所有图像转换为PAM：

`winicontopam -allimages {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 将输入文件中的第n幅图像转换为PAM：

`winicontopam -image {{n}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- 如果要提取的图像包含渐变透明数据和AND掩码，则将AND掩码写入输出PAM文件的第五个通道：

`winicontopam -andmasks {{path/to/input_file.ico}} > {{path/to/output.pam}}`