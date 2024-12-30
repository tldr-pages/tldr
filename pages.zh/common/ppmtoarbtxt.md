# ppmtoarbtxt

> 将 PPM 图像转换为根据模板指定的任意文本格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>。

- 将 PPM 图像转换为由给定模板指定的文本：

`ppmtoarbtxt {{path/to/template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 将 PPM 图像转换为由给定模板指定的文本，并在前面添加指定头模板的内容：

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/head_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 将 PPM 图像转换为由给定模板指定的文本，并在后面添加指定尾模板的内容：

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/tail_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 显示版本：

`ppmtoarbtxt -version`