# pamoil

> 将PAM图像转换为油画。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamoil.html>。

- 将PAM图像转换为油画：

`pamoil {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`

- 考虑N个像素的邻域以实现“涂抹”效果：

`pamoil -n {{N}} {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`