# pamoil

> 将 PAM 图像转换为油画。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamoil.html>.

- 将 PAM 图像转换为油画：

`pamoil {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`

- 考虑 `n` 个像素的邻域以产生“涂抹”效果：

`pamoil -n {{n}} {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`
