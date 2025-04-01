# ppmtoarbtxt

> 将 PPM 图像转换为根据模板指定的任意文本格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>.

- 根据指定的模板将 PPM 图像转换为文本：

`ppmtoarbtxt {{path/to/template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 根据指定的模板将 PPM 图像转换为文本，并在开头附加指定头部模板的内容：

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/head_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 根据指定的模板将 PPM 图像转换为文本，并在末尾附加指定尾部模板的内容：

`ppmtoarbtxt {{path/to/template}} -hd {{path/to/tail_template}} {{path/to/image.ppm}} > {{path/to/output_file.txt}}`

- 显示版本：

`ppmtoarbtxt -version`
