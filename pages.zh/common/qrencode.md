# qrencode

> 二维码生成器。支持 PNG 和 EPS 格式。
> 更多信息：<https://manned.org/qrencode>.

- 将字符串转换为二维码并保存到输出文件：

`qrencode -o {{路径/到/输出文件.png}} {{字符串}}`

- 将输入文件转换为二维码并保存到输出文件：

`qrencode -o {{路径/到/输出文件.png}} -r {{路径/到/输入文件}}`

- 将字符串转换为二维码并在终端中打印：

`qrencode -t ansiutf8 {{字符串}}`

- 从管道输入转换为二维码并在终端中打印：

`echo {{字符串}} | qrencode -t ansiutf8`
