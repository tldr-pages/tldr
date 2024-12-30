# qrencode

> QR 码生成器。支持 PNG 和 EPS 格式。
> 更多信息：<https://fukuchi.org/works/qrencode>。

- 将字符串转换为 QR 码并保存到输出文件：

`qrencode -o {{path/to/output_file.png}} {{string}}`

- 将输入文件转换为 QR 码并保存到输出文件：

`qrencode -o {{path/to/output_file.png}} -r {{path/to/input_file}}`

- 将字符串转换为 QR 码并在终端打印：

`qrencode -t ansiutf8 {{string}}`

- 将管道输入转换为 QR 码并在终端打印：

`echo {{string}} | qrencode -t ansiutf8`